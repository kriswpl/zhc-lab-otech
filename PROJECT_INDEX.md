# Project Index

Ten plik jest canonical lokalnym routerem projektu `ZHC_LAB_OTECH`.

Nie jest metodologią ZHC ani kopią shared architecture. Definiuje lokalną instancję wspólnego kontraktu ZHC: gdzie AI czyta, gdzie zapisuje, który system jest authoritative dla danej klasy informacji oraz gdzie znajdują się lokalne pointery projektu.

Od cutoveru 2026-09-23 projekt jest **Drive-native** dla project knowledge i project state. Notion oraz wcześniejsze projekcje GitHub/Drive nie są current source of truth.

---

## 0. Identity i shared contract

- `DOMAIN_KEY`: `ZHC_LAB_OTECH`
- `TYPE`: `OPPORTUNITY_PORTFOLIO`
- `STATE_MODE`: `PROJECT_MANAGED`
- AI Mind `ROOT_FOLDER`: https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix
- Canonical `PROJECT_ROOT`: https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix
- GitHub code / execution repo: `kriswpl/zhc-lab-otech`

### AI Mind shared runtime inheritance

- `SHARED_RUNTIME_CONTRACT`: https://docs.google.com/document/d/1bdz0nM7PD97HvawgB--xOoeQCf8kzYCI_WXeDJa1TNA/edit
- `SHARED_RUNTIME_SCOPE`: `5A. SHARED RUNTIME INVARIANTS`
- `SHARED_RUNTIME_REV`: `read-live`

Przed pracą wymagającą kontekstu projektu wykonaj bounded live read wyłącznie wskazanego `SHARED_RUNTIME_SCOPE` z `SHARED_RUNTIME_CONTRACT` i zastosuj go razem z tym lokalnym kontraktem.

Nie odczytuj Global Registry ani pozostałych sekcji Global Runtime podczas zwykłej pracy lokalnej. Lokalny `PROJECT_INDEX.md` pozostaje canonical dla source routing, source precedence i local overrides. Aktywne overrides są zdefiniowane w sekcji 10.

### Shared ZHC methodology / process / runtime read planes

- `PRODUCT_BASE_FLAT`: https://drive.google.com/drive/folders/1q9aveb064ov_jexj32Pn6DuhnUSMkH4Q
- `_ROOT.md`: https://drive.google.com/file/d/1NRJFIpEWD741tPwBV1z4QVdN-aMp9zrO/view
- `WORK_PACKET_MATRIX_V4_4`: https://docs.google.com/spreadsheets/d/15a7Esy9Ehkl-4qi1SkcHvUfiIXWFDBxPHg6oimNXwZs/edit
- `ZHC OS Engineering.md`: https://drive.google.com/file/d/1eqVdmlNoMNd-TbDM5ZElVGi6JcsbSYsT/view
- `ZHC_RUNTIME_RELEASE`: `zhc-runtime-v0.0.3-pp01e01.4`
- `ZHC_RUNTIME_INDEX`: https://drive.google.com/file/d/16svi9QiFyzNrMO41ooV3iG-eYUv20vuf/view
- `ZHC_RUNTIME_FLAT`: https://drive.google.com/drive/folders/1oFP2uvbC-pOYY7khdi6vzS7RPq8yXpBn
- `ZHC_RUNTIME_SOURCE_COMMIT`: `2ba4e2f59b4a428e48f60d95e0d797451f4e2e19`
- `ZHC_RUNTIME_SCOPE`: `PP-00-G01; PP-00-E03; PP-00-E01; PP-00-E02; PP-00-J01; PP-01-E01`

Dla WPT z `ZHC_RUNTIME_SCOPE` odczytaj `ZHC_RUNTIME_INDEX`, następnie wyłącznie odpowiadający `ZHC_RUNTIME_FLAT/<WPT_ID>.md`. Ten pojedynczy FLAT WPT jest kompletnym execution read unit. Nie rekonstruuj wykonania z Matrixu, Product Base, `zhc-os/main:/system` ani pamięci rozmów. `next_wpt` jest pointerem i nie uruchamia kolejnego WPT automatycznie.

---

## 1. Local source map

| Information class | Normal read plane | Authoritative write owner | Local pointer |
|---|---|---|---|
| Opportunity portfolio / runtime state | Drive — `10 - Project State/Project State` | Drive — `Project State` Google Sheet | https://docs.google.com/spreadsheets/d/1e_96uq9YsI72j5vNp_9hZUxdu0QGWOE0iW_YQK20Qso/edit |
| Rich detail / human review pages linked from state | Drive Google Docs | Drive Google Docs | `detail_doc` w odpowiednim rekordzie |
| Lab durable knowledge | Drive — `20 - Knowledge` | Drive | https://drive.google.com/drive/folders/1pXPr4Y_Zo0uoo94N2M7EChm3FiTsAwbC |
| Research / brain dumps / source material | Drive — `30 - Research` | Drive | https://drive.google.com/drive/folders/1wOzSPgPOI4Ttnr6pT1xPXlSA5hTo5W06 |
| Product / experiment artifacts | Drive — `40 - Artifacts` | Drive | https://drive.google.com/drive/folders/1Q_qSj2zElIzokcecu7oy_1_7EOgcU_89 |
| Backlog / tasks / implementation status Labu | Linear | Linear | właściwy projekt/workspace ZHC Lab OTECH |
| OTECH company governance / reporting / financing / operational state | domena `OTECH` | domena `OTECH` | handoff do `DOMAIN_KEY=OTECH` |
| Source code / infra / workflows / repo-native config | GitHub | GitHub | `kriswpl/zhc-lab-otech` |
| `PROJECT_INDEX.md` | Drive `PROJECT_ROOT` | Drive | https://drive.google.com/file/d/1k5VZp8tl3_gYvkQJjqQD9VuPd5XQ_yXL/view |
| Historical / migration material | Drive — `90 - Archive` | Drive archive only | https://drive.google.com/drive/folders/1QimTbxxuWMk8GBuiOrDVbp2_WbBhgNjs |
| Shared ZHC methodology / Knowledge | `PRODUCT_BASE_FLAT` | ZHC source plane zgodny z jego własnym kontraktem | Product Base pointers z sekcji 0 |
| Shared ZHC runtime execution | `ZHC_RUNTIME_INDEX -> ZHC_RUNTIME_FLAT/<WPT_ID>.md` | ZHC runtime source; local writes według WPT + tego Indexu | runtime pointers z sekcji 0 |

Każda klasa informacji ma jednego authoritative write ownera.

**Notion nie jest normal read plane ani write plane dla ZHC Lab OTECH.** Pozostaje wyłącznie historycznym migration source i nie jest fallbackiem do current state.

---

## 2. Canonical project root — Google Drive

Canonical project root:
https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix

Minimalna struktura:

```text
ZHC Lab OTECH/
├── PROJECT_INDEX.md
├── 10 - Project State/
│   └── Project State [Google Sheet]
├── 20 - Knowledge/
│   └── Konstytucja Labu [Google Doc]
├── 30 - Research/
├── 40 - Artifacts/
└── 90 - Archive/
```

Pointery:

| Obszar | Pointer |
|---|---|
| `PROJECT_INDEX.md` | https://drive.google.com/file/d/1k5VZp8tl3_gYvkQJjqQD9VuPd5XQ_yXL/view |
| `10 - Project State` | https://drive.google.com/drive/folders/1NWLBNMqgdZOZtgOe7c-06KFWoK0V9Ds0 |
| `Project State` | https://docs.google.com/spreadsheets/d/1e_96uq9YsI72j5vNp_9hZUxdu0QGWOE0iW_YQK20Qso/edit |
| `20 - Knowledge` | https://drive.google.com/drive/folders/1pXPr4Y_Zo0uoo94N2M7EChm3FiTsAwbC |
| `Konstytucja Labu` | https://docs.google.com/document/d/1yddhEJbd-W7QBy-bu2X7mFPEtT53CIuzZWpQoFKJLPQ/edit |
| `30 - Research` | https://drive.google.com/drive/folders/1wOzSPgPOI4Ttnr6pT1xPXlSA5hTo5W06 |
| `40 - Artifacts` | https://drive.google.com/drive/folders/1Q_qSj2zElIzokcecu7oy_1_7EOgcU_89 |
| `90 - Archive` | https://drive.google.com/drive/folders/1QimTbxxuWMk8GBuiOrDVbp2_WbBhgNjs |

---

## 3. Structured project state — `10 - Project State/Project State`

Canonical structured current state Labu jest Google Sheet `Project State`.

Aktywne zakładki:
- `IDEAS_INBOX`
- `SOURCES`
- `SIGNAL`
- `WORKFLOW_CASE`
- `STAGED_OUTPUTS`
- `GATE_RECORD`
- `OPPORTUNITY_CARD`
- `EVIDENCE_ITEM`
- `DECISION_RECORD`

State schema został zainicjalizowany z tego samego Drive-native wzorca co ZHC Lab Solo, bez kopiowania jego danych biznesowych.

Rekord w Sheet przechowuje structured current state. Gdy obiekt wymaga dłuższego opisu, rationale, tabel lub narracji, może wskazać Google Doc przez `detail_doc`. `detail_doc` nie tworzy drugiego source of truth.

---

## 4. Project knowledge, research i artifacts

### `20 - Knowledge`
Canonical durable project knowledge. Aktualna `Konstytucja Labu`:
https://docs.google.com/document/d/1yddhEJbd-W7QBy-bu2X7mFPEtT53CIuzZWpQoFKJLPQ/edit

### `30 - Research`
Brain dumpy, materiały źródłowe i durable research.

### `40 - Artifacts`
Trwałe artefakty eksperymentów, produktu i komunikacji.

### `90 - Archive`
Materiały historyczne, legacy mirrors i snapshoty migracyjne. Archive nie jest fallbackiem do current state.

---

## 5. Opportunity portfolio ownership i handoff do OTECH

ZHC Lab OTECH może utrzymywać wiele sygnałów i Opportunities związanych z OTECH jednocześnie.

Dopóki temat pozostaje Opportunity / eksperymentem ZHC, current opportunity state pozostaje w `ZHC_LAB_OTECH`.

Gdy temat przechodzi do regularnej realizacji w OTECH, bieżący governance / operational / execution state przejmuje domena `OTECH`, a Lab zachowuje lineage, evidence i decision trail.

Jeżeli powstaje samodzielny produkt lub venture, stosujemy `SPIN_OUT` do nowej domeny `PROJECT_MANAGED`.

---

## 6. Execution — Linear i handoff

Authoritative owner dla backlogu, tasks i implementation work **Labu** jest Linear.

Po handoffie do regularnej realizacji w OTECH wykonanie przestaje być current execution state Labu. Wtedy przejdź do domeny `OTECH` i zastosuj jej lokalny kontrakt/runtime.

---

## 7. Repo-native work — GitHub

GitHub `kriswpl/zhc-lab-otech` jest authoritative write ownerem wyłącznie dla:
- source code,
- infra,
- deployment,
- workflowów związanych z kodem/execution,
- repo-native configuration.

Project knowledge, project state i `PROJECT_INDEX.md` nie są mirrorowane do GitHuba.

Dawny Notion -> GitHub -> Drive context sync jest wyłączony. Nie ma aktywnej domyślnej materializacji Google Docs/Sheets do `.md` / `.csv` / `.ndjson`.

---

## 8. Routing według zadania

### Current opportunity / runtime state
`PROJECT_INDEX.md -> 10 - Project State/Project State -> tylko potrzebna zakładka / rekord -> opcjonalnie detail_doc`

### Trwała wiedza Labu
`PROJECT_INDEX.md -> 20 - Knowledge -> tylko potrzebny dokument`

### Research / brain dump
`PROJECT_INDEX.md -> 30 - Research -> tylko potrzebne źródło`

### Execution / backlog / task status Labu
`PROJECT_INDEX.md -> Linear`

### Bieżący governance / reporting / financing / operational state spółki OTECH
`PROJECT_INDEX.md -> handoff do DOMAIN_KEY=OTECH -> lokalny entrypoint domeny OTECH`

### Kod / infra / deployment / repo-native config
`PROJECT_INDEX.md -> GitHub kriswpl/zhc-lab-otech`

### WPT execution
`PROJECT_INDEX.md -> ZHC_RUNTIME_INDEX -> ZHC_RUNTIME_FLAT/<WPT_ID>.md -> tylko wymagane local inputs/state -> wykonanie -> walidacja -> authoritative local write`

Minimalny normalny prompt może zawierać tylko wskazanie wejścia, jeśli nie da się go jednoznacznie rozwiązać lokalnie, oraz polecenie wykonania konkretnego `WPT_ID`.

---

## 9. Freshness, conflicts i source precedence

- Drive jest canonical bezpośrednio dla project knowledge/state.
- Successful write do canonical Drive source jest current truth dla swojej klasy informacji.
- Notion po cutoverze jest historycznym migration source, nie current fallbackiem.
- GitHub nie jest projekcją knowledge/state.
- `90 - Archive` nie jest current fallbackiem.
- Domena `OTECH` ma pierwszeństwo przy claimach o bieżącym governance i operational state spółki.
- Dla WPT objętych `ZHC_RUNTIME_SCOPE` pierwszeństwo jako execution contract ma przypięty `ZHC_RUNTIME_INDEX` + dokładny FLAT WPT.

---

## 10. Local overrides

`LOCAL_OVERRIDES:`

- `WPT_EXECUTION = PINNED_ZHC_RUNTIME_INDEX`
- `ZHC_RUNTIME_INDEX = https://drive.google.com/file/d/16svi9QiFyzNrMO41ooV3iG-eYUv20vuf/view`
- `ZHC_RUNTIME_FLAT = https://drive.google.com/drive/folders/1oFP2uvbC-pOYY7khdi6vzS7RPq8yXpBn`
- `ZHC_RUNTIME_SOURCE_COMMIT = 2ba4e2f59b4a428e48f60d95e0d797451f4e2e19`
- `ZHC_RUNTIME_SCOPE = PP-00-G01;PP-00-E03;PP-00-E01;PP-00-E02;PP-00-J01;PP-01-E01`
- `RUNTIME_PROGRESSIVE_LOADING = ONE_WPT_AT_A_TIME`
- `USER_PROMPT_CONTRACT = BUSINESS_INPUT_PLUS_WPT_ONLY`
- `EXECUTABLE_CURRENT_EXCLUDED_FROM_NORMAL_PROJECT_ROUTING = true`
- `ZHC_RUNTIME_SKILL_REQUIRED = false`
- `ZHC_RUNTIME_RELEASE = zhc-runtime-v0.0.3-pp01e01.4`
- `HUMAN_REVIEW_PROJECTION = REQUIRED_BEFORE_CANONICAL_APPROVAL`
- `HUMAN_REVIEW_PROJECTION_ADAPTER = GOOGLE_DOC_NATIVE_TABS`
- `HUMAN_REVIEW_PROJECTION_TARGET = SAME_LOCAL_STAGING_PLANE_AS_STAGED_PACKAGE`
- `HUMAN_REVIEW_PROJECTION_SOURCE_OF_TRUTH = false`
- `APPROVAL_PACKAGE = WHOLE_VALIDATED_PACKAGE`
- `STAGED_PROPOSAL_LEDGER = APPEND_ONLY`
- `DETAIL_DOC_POINTER = RESOLVABLE`
- `CANONICAL_HUMAN_PROJECTION = REQUIRED_AFTER_APPROVED_COMMIT_WHEN_DECLARED`
- `CANONICAL_HUMAN_PROJECTION_SOURCE_OF_TRUTH = false`

---

## 11. Cutover history

Cutover do Drive-native source architecture wykonano 2026-09-23.

Zmiany:
- istniejący folder ZHC Lab OTECH pozostał canonical `PROJECT_ROOT`,
- `PROJECT_INDEX.md` zachowuje ten sam Drive file ID i staje się canonical local contract,
- Notion-generated `docs/` i `state/` zostały zachowane w `90 - Archive/Pre-Drive-native cutover - 2026-09-23`,
- canonical state został przeniesiony do Google Sheet `10 - Project State/Project State`,
- durable `Konstytucja Labu` została przeniesiona do Google Docs w `20 - Knowledge`,
- ZHC runtime `.4` został przypięty jako lokalny execution contract dla aktywnego scope,
- Notion -> GitHub -> Drive sync został wyłączony,
- GitHub pozostaje repo-native plane dla code/execution,
- Notion pozostaje historycznym migration source i nie jest current fallbackiem.
