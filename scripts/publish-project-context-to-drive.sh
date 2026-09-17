#!/usr/bin/env bash

set -euo pipefail

STAGING_DIR="/tmp/project-context"

echo "=== Publish Project Context to Google Drive ==="

if [ -z "${GDRIVE_PROJECT_CONTEXT_FOLDER_ID:-}" ]; then
  echo "ERROR: GDRIVE_PROJECT_CONTEXT_FOLDER_ID is not set."
  exit 1
fi

if ! command -v rclone >/dev/null 2>&1; then
  echo "ERROR: rclone is not installed."
  exit 1
fi

if [ ! -f "PROJECT_INDEX.md" ]; then
  echo "ERROR: PROJECT_INDEX.md not found."
  exit 1
fi

if [ ! -d "docs" ]; then
  echo "ERROR: docs/ directory not found."
  exit 1
fi

if [ ! -d "state" ]; then
  echo "ERROR: state/ directory not found."
  exit 1
fi

echo "Building staging package..."

rm -rf "$STAGING_DIR"
mkdir -p "$STAGING_DIR"

cp "PROJECT_INDEX.md" "$STAGING_DIR/"
cp -R "docs" "$STAGING_DIR/"
cp -R "state" "$STAGING_DIR/"

echo
echo "Package contents:"
find "$STAGING_DIR" -type f -print | sort

echo
echo "Checking Google Drive connection..."

rclone lsd "gdrive:" \
  --drive-root-folder-id "$GDRIVE_PROJECT_CONTEXT_FOLDER_ID" \
  >/dev/null

echo
echo "Syncing project context to Google Drive..."

rclone sync \
  "$STAGING_DIR/" \
  "gdrive:" \
  --drive-root-folder-id "$GDRIVE_PROJECT_CONTEXT_FOLDER_ID" \
  --delete-during \
  --max-delete 20 \
  --verbose

echo
echo "Project context successfully published to Google Drive."
