#!/usr/bin/env python3

import argparse
import csv
import io
import json
import os
import sys
from pathlib import Path
from typing import Any

import requests
import yaml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "config" / "project.sources.yaml"


class SyncError(RuntimeError):
    pass


def load_config(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise SyncError(f"Config not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if not isinstance(config, dict):
        raise SyncError("Config must contain a YAML object.")

    sources = config.get("sources")
    if not isinstance(sources, list) or not sources:
        raise SyncError(
            "config/project.sources.yaml must contain a non-empty 'sources:' list."
        )

    active_sources = []
    outputs = set()

    for source in sources:
        if not isinstance(source, dict):
            raise SyncError(f"Invalid source entry: {source!r}")

        name = source.get("name", "unnamed")
        enabled = source.get("enabled", False)
        if not isinstance(enabled, bool):
            raise SyncError(f"'enabled' must be true or false for source: {name}")
        if not enabled:
            print(f"[skip] {name} (not enabled)", file=sys.stderr)
            continue

        if source.get("provider") != "notion":
            raise SyncError(f"Unsupported provider for {name}: {source.get('provider')}")

        source_type = source.get("type")
        if source_type not in {"page", "database"}:
            raise SyncError(f"Unsupported type for {name}: {source_type}")

        output = source.get("output")
        if not output:
            raise SyncError(f"Missing output for source: {name}")
        if output in outputs:
            raise SyncError(f"Duplicate output path: {output}")

        if source_type == "page":
            page_id = source.get("source_id") or source.get("page_id")
            if not page_id:
                raise SyncError(f"Page source '{name}' requires source_id or page_id.")

        if source_type == "database":
            database_id = (
                source.get("database_id")
                or source.get("source_id")
                or source.get("data_source_id")
            )
            if not database_id:
                raise SyncError(
                    f"Database source '{name}' requires database_id, source_id or data_source_id."
                )

        outputs.add(output)
        active_sources.append(source)

    if not active_sources:
        raise SyncError("No enabled sources found in config/project.sources.yaml.")

    config["sources"] = active_sources
    return config


def safe_output_path(relative_path: str) -> Path:
    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise SyncError(f"Unsafe output path: {relative_path}")

    target = (REPO_ROOT / relative).resolve()
    try:
        target.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise SyncError(f"Output escapes repository: {relative_path}") from exc
    return target


def build_session(token: str) -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504, 529],
        allowed_methods=frozenset({"GET", "POST"}),
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }
    )
    return session


def notion_request(
    session: requests.Session,
    method: str,
    path: str,
    **kwargs: Any,
) -> dict[str, Any]:
    response = session.request(
        method,
        f"{NOTION_API_BASE}{path}",
        timeout=60,
        **kwargs,
    )

    if not response.ok:
        try:
            payload = response.json()
            message = payload.get("message", response.text)
            code = payload.get("code", "")
        except Exception:
            message = response.text
            code = ""
        raise SyncError(
            f"Notion API error {response.status_code} {code}: {message}\n"
            f"Request: {method} {path}"
        )

    return response.json()


def rich_text_to_markdown(items: list[dict[str, Any]]) -> str:
    result = []
    for item in items or []:
        text = item.get("plain_text", "")
        if not text:
            continue
        annotations = item.get("annotations") or {}
        href = item.get("href")
        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if href:
            text = f"[{text}]({href})"
        result.append(text)
    return "".join(result)


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def get_block_children(
    session: requests.Session,
    block_id: str,
) -> list[dict[str, Any]]:
    results = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        payload = notion_request(
            session,
            "GET",
            f"/blocks/{block_id}/children",
            params=params,
        )
        results.extend(payload.get("results", []))
        if not payload.get("has_more"):
            break
        cursor = payload.get("next_cursor")
    return results


def render_table(session: requests.Session, block: dict[str, Any]) -> str:
    rows = get_block_children(session, block["id"])
    table_rows = []
    for row in rows:
        if row.get("type") != "table_row":
            continue
        cells = row.get("table_row", {}).get("cells", [])
        table_rows.append(
            [escape_table_cell(rich_text_to_markdown(cell)) for cell in cells]
        )

    if not table_rows:
        return ""

    width = max(len(row) for row in table_rows)
    for row in table_rows:
        while len(row) < width:
            row.append("")

    output = [
        "| " + " | ".join(table_rows[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in table_rows[1:]:
        output.append("| " + " | ".join(row) + " |")
    return "\n".join(output)


def file_url(block_data: dict[str, Any]) -> str:
    file_object = block_data.get("file") or {}
    external_object = block_data.get("external") or {}
    return file_object.get("url") or external_object.get("url") or ""


def render_blocks(
    session: requests.Session,
    blocks: list[dict[str, Any]],
    depth: int = 0,
) -> str:
    output = []

    for block in blocks:
        block_type = block.get("type")
        data = block.get(block_type, {}) or {}
        line = ""
        recurse = True

        if block_type == "paragraph":
            line = rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "heading_1":
            line = "# " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "heading_2":
            line = "## " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "heading_3":
            line = "### " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "bulleted_list_item":
            line = "  " * depth + "- " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "numbered_list_item":
            line = "  " * depth + "1. " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "to_do":
            marker = "- [x] " if data.get("checked", False) else "- [ ] "
            line = "  " * depth + marker + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type in {"quote", "callout"}:
            line = "> " + rich_text_to_markdown(data.get("rich_text", []))
        elif block_type == "toggle":
            line = "  " * depth + "- **" + rich_text_to_markdown(data.get("rich_text", [])) + "**"
        elif block_type == "divider":
            line = "---"
        elif block_type == "code":
            language = data.get("language") or ""
            code = rich_text_to_markdown(data.get("rich_text", []))
            line = f"```{language}\n{code}\n```"
        elif block_type == "table":
            line = render_table(session, block)
            recurse = False
        elif block_type in {"column_list", "column", "synced_block"}:
            line = ""
        elif block_type == "child_page":
            line = f"**Subpage:** {data.get('title', '')}"
        elif block_type == "child_database":
            line = f"**Database:** {data.get('title', '')}"
        elif block_type in {"bookmark", "embed", "link_preview"}:
            url = data.get("url", "")
            if url:
                line = f"<{url}>"
        elif block_type in {"image", "video", "audio", "pdf", "file"}:
            url = file_url(data)
            caption = rich_text_to_markdown(data.get("caption", []))
            label = caption or block_type.capitalize()
            if url:
                line = f"![{label}]({url})" if block_type == "image" else f"[{label}]({url})"
        elif block_type == "equation":
            line = f"$${data.get('expression', '')}$$"
        else:
            rich_text = data.get("rich_text")
            if rich_text:
                line = rich_text_to_markdown(rich_text)

        if line:
            output.append(line)

        if recurse and block.get("has_children"):
            children = get_block_children(session, block["id"])
            rendered_children = render_blocks(session, children, depth + 1)
            if rendered_children:
                output.append(rendered_children)

    return "\n\n".join(part for part in output if part.strip())


def extract_page_title(page: dict[str, Any]) -> str:
    for prop in (page.get("properties") or {}).values():
        if prop.get("type") == "title":
            value = rich_text_to_markdown(prop.get("title", []))
            if value:
                return value
    return "Untitled"


def export_page(session: requests.Session, page_id: str) -> str:
    page = notion_request(session, "GET", f"/pages/{page_id}")
    title = extract_page_title(page)
    body = render_blocks(session, get_block_children(session, page_id))
    header = (
        "<!-- GENERATED FROM NOTION. DO NOT EDIT MANUALLY. -->\n"
        f"<!-- notion-page-id: {page_id} -->\n\n"
        f"# {title}\n"
    )
    return header + ("\n" + body + "\n" if body else "\n")


def plain_text(items: list[dict[str, Any]]) -> str:
    return "".join(item.get("plain_text", "") for item in items or [])


def property_to_value(prop: dict[str, Any]) -> str:
    prop_type = prop.get("type")
    value = prop.get(prop_type)

    if prop_type in {"title", "rich_text"}:
        return plain_text(value or [])
    if prop_type == "number":
        return "" if value is None else str(value)
    if prop_type in {"select", "status"}:
        return value.get("name", "") if value else ""
    if prop_type == "multi_select":
        return " | ".join(item.get("name", "") for item in value or [])
    if prop_type == "date":
        if not value:
            return ""
        start = value.get("start", "")
        end = value.get("end")
        return f"{start} -> {end}" if end else start
    if prop_type == "checkbox":
        return "true" if value else "false"
    if prop_type in {"url", "email", "phone_number", "created_time", "last_edited_time"}:
        return value or ""
    if prop_type in {"created_by", "last_edited_by"}:
        return (value.get("name") or value.get("id") or "") if value else ""
    if prop_type == "people":
        return " | ".join(person.get("name") or person.get("id") or "" for person in value or [])
    if prop_type == "relation":
        return " | ".join(relation.get("id", "") for relation in value or [])
    if prop_type == "files":
        values = []
        for item in value or []:
            name = item.get("name", "")
            file_data = item.get("file") or item.get("external") or {}
            url = file_data.get("url", "")
            if name and url:
                values.append(f"{name}: {url}")
            elif url:
                values.append(url)
            elif name:
                values.append(name)
        return " | ".join(values)
    if prop_type in {"formula", "rollup"}:
        if not value:
            return ""
        nested_type = value.get("type")
        nested_value = value.get(nested_type)
        if nested_value is None:
            return ""
        if isinstance(nested_value, (dict, list)):
            return json.dumps(nested_value, ensure_ascii=False, sort_keys=True)
        return str(nested_value)
    if prop_type == "unique_id":
        if not value:
            return ""
        prefix = value.get("prefix") or ""
        number = value.get("number")
        return "" if number is None else f"{prefix}{number}"
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def resolve_data_source_id(
    session: requests.Session,
    source: dict[str, Any],
) -> str:
    explicit = source.get("data_source_id")
    if explicit:
        return explicit

    database_id = source.get("database_id") or source.get("source_id")
    if not database_id:
        raise SyncError(f"Database source '{source.get('name')}' requires database_id.")

    database = notion_request(session, "GET", f"/databases/{database_id}")
    data_sources = database.get("data_sources", [])
    if not data_sources:
        raise SyncError(
            f"Database '{source.get('name')}' contains no data sources: {database_id}"
        )
    if len(data_sources) > 1:
        choices = ", ".join(
            f"{item.get('name')}={item.get('id')}" for item in data_sources
        )
        raise SyncError(
            f"Database '{source.get('name')}' has multiple data sources. "
            f"Add data_source_id to config/project.sources.yaml. Available: {choices}"
        )
    return data_sources[0]["id"]


def query_data_source(
    session: requests.Session,
    data_source_id: str,
) -> list[dict[str, Any]]:
    results = []
    cursor = None
    while True:
        payload: dict[str, Any] = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        response = notion_request(
            session,
            "POST",
            f"/data_sources/{data_source_id}/query",
            json=payload,
        )
        results.extend(response.get("results", []))
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")
    return results


def export_database(session: requests.Session, source: dict[str, Any]) -> str:
    data_source_id = resolve_data_source_id(session, source)
    data_source = notion_request(session, "GET", f"/data_sources/{data_source_id}")
    property_names = list((data_source.get("properties") or {}).keys())
    metadata_columns = [
        "_notion_page_id",
        "_notion_url",
        "_created_time",
        "_last_edited_time",
    ]
    fieldnames = property_names + metadata_columns
    pages = query_data_source(session, data_source_id)

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()

    for page in pages:
        row = {}
        page_properties = page.get("properties") or {}
        for property_name in property_names:
            prop = page_properties.get(property_name)
            row[property_name] = "" if prop is None else property_to_value(prop)
        row["_notion_page_id"] = page.get("id", "")
        row["_notion_url"] = page.get("url", "")
        row["_created_time"] = page.get("created_time", "")
        row["_last_edited_time"] = page.get("last_edited_time", "")
        writer.writerow(row)

    return buffer.getvalue()


def write_if_changed(path: Path, content: str) -> bool:
    old_content = path.read_text(encoding="utf-8") if path.exists() else None
    if old_content == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export project context from Notion to Markdown and CSV."
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="Path to config/project.sources.yaml",
    )
    parser.add_argument(
        "--list-outputs",
        action="store_true",
        help="Print output paths for enabled sources without calling Notion.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(Path(args.config).resolve())
    sources = config["sources"]

    if args.list_outputs:
        for source in sources:
            print(source["output"])
        return 0

    token = os.environ.get("NOTION_TOKEN")
    if not token:
        raise SyncError("NOTION_TOKEN environment variable is not set.")

    session = build_session(token)
    changed = 0
    print(f"Notion API version: {NOTION_VERSION}")

    for source in sources:
        name = source.get("name", "unnamed")
        source_type = source["type"]
        output = source["output"]
        target = safe_output_path(output)

        print(f"\n[sync] {name}")
        print(f"       type:   {source_type}")
        print(f"       output: {output}")

        if source_type == "page":
            page_id = source.get("source_id") or source.get("page_id")
            content = export_page(session, page_id)
        elif source_type == "database":
            content = export_database(session, source)
        else:
            raise SyncError(f"Unsupported source type: {source_type}")

        if write_if_changed(target, content):
            changed += 1
            print("       result: CHANGED")
        else:
            print("       result: unchanged")

    print(f"\nSync complete. Changed files: {changed}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SyncError as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
