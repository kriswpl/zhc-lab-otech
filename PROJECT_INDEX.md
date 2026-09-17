# Project Index

Ten plik jest lokalnym routerem domeny `ZHC_LAB_OTECH`.

Nie jest current state, metodologią ZHC ani kopią shared architecture. Definiuje wyłącznie to, jak ZHC Lab OTECH instancjonuje wspólny kontrakt ZHC: gdzie AI czyta, gdzie zapisuje, który system jest authoritative dla danej klasy informacji oraz gdzie znajdują się lokalne pointery domeny.

## 0. Identity i shared contract

- `DOMAIN_KEY`: `ZHC_LAB_OTECH`
- `TYPE`: `OPPORTUNITY_PORTFOLIO`
- `STATE_MODE`: `PROJECT_MANAGED`
- GitHub: `kriswpl/zhc-lab-otech`
- AI Mind `ROOT_FOLDER`: https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix
- Project read mirror root: https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix

### AI Mind shared runtime inheritance

- `SHARED_RUNTIME_CONTRACT`: https://docs.google.com/document/d/1bdz0nM7PD97HvawgB--xOoeQCf8kzYCI_WXeDJa1TNA/edit
- `SHARED_RUNTIME_SCOPE`: `5A. SHARED RUNTIME INVARIANTS`
- `SHARED_RUNTIME_REV`: `read-live`

Przed pracą wymagającą kontekstu projektu wykonaj bounded live read wyłącznie wskazanego `SHARED_RUNTIME_SCOPE` z `SHARED_RUNTIME_CONTRACT` i zastosuj go razem z tym lokalnym kontraktem.

Nie odczytuj Global Registry ani pozostałych sekcji Global Runtime podczas zwykłej pracy lokalnej. Global Runtime jest tutaj używany wyłącznie jako shared invariant plane, nie jako router.

Lokalny `PROJECT_INDEX.md` pozostaje canonical dla lokalnego source routing, source precedence i local overrides. W razie konfliktu jawny `LOCAL_OVERRIDES` ma pierwszeństwo nad shared invariant tylko w zakresie opisanego override; obecnie `LOCAL_OVERRIDES: none`.

ZHC Lab OTECH dziedziczy wspólny kontrakt projektowy ZHC z **ZHC Product Base**.

### Shared ZHC Product Base — read plane

- FLAT: https://drive.google.com/drive/folders/1q9aveb064ov_jexj32Pn6DuhnUSMkH4Q
- `_ROOT.md`: https://drive.google.com/file/d/1NRJFIpEWD741tPwBV1z4QVdN-aMp9zrO/view
- `ZHC OS Engineering.md`: https://drive.google.com/file/d/1eqVdmlNoMNd-TbDM5ZElVGi6JcsbSYsT/view

Dla zasad source authority, read/write planes, projections, managed objects, sync lag, mutation rules i runtime adapters stosuj w `ZHC OS Engineering.md` sekcję **`Project Source / Access / Mutation Contract`**.

`PROJECT_INDEX.md` nie powiela shared metodologii ani kontraktu. Poniżej definiuje ich lokalną instancję dla ZHC Lab OTECH.

---

## 1. Local source map

| Information class | Normal read plane | Authoritative write owner | Local pointer |
|---|---|---|---|
| Lab durable knowledge | Drive `docs/` | Notion `ZHC Lab OTECH` | `docs/` |
| Opportunity portfolio state: signals / opportunities / hypotheses / experiments / evidence / decisions / operational state | Drive `state/` | Notion `ZHC Lab OTECH` | `state/` |
| Lab backlog / tasks / execution status | Linear | Linear | właściwy projekt/workspace ZHC Lab OTECH w Linear, gdy zostanie zainstancjonowany |
| OTECH company governance / reporting / financing / operational state | domena `OTECH` | domena `OTECH` | handoff przez AI Mind Registry do `DOMAIN_KEY=OTECH` |
| Repo-native config / workflows / sync scripts / source code | GitHub | GitHub | `kriswpl/zhc-lab-otech` |
| `PROJECT_INDEX.md` | GitHub / Drive mirror | GitHub | repo root |
| Shared ZHC operating knowledge | ZHC Product Base FLAT | ZHC source plane zgodny z jego własnym kontraktem | Product Base pointers z sekcji 0 |

Każda klasa informacji ma jednego authoritative write ownera. Drive `docs/` i `state/` oraz ich odpowiedniki w GitHub są generowanymi projekcjami do odczytu/versioningu, nie alternatywnym semantic write masterem.

---

## 2. Opportunity portfolio ownership i handoff do OTECH

ZHC Lab OTECH może utrzymywać wiele sygnałów i wiele Opportunities związanych z OTECH jednocześnie.

Lab owns current state danego Opportunity dopóki temat pozostaje eksperymentem / Opportunity ZHC. Shared metoda ZHC rozróżnia intake `INSPIRATION / CANDIDATE` oraz decyzje portfelowe `NOW / REDESIGN / PARK / KILL`.

Jeżeli Opportunity przechodzi do regularnej realizacji w istniejącej organizacji OTECH:

- bieżący governance / operational / execution state przejmuje domena `OTECH`,
- ZHC Lab OTECH zachowuje lineage: źródłowy signal, Opportunity, evidence, hipotezy, eksperymenty i decision trail,
- ZHC Lab OTECH nie utrzymuje konkurencyjnego operational state OTECH.

Jeżeli w wyniku pracy powstaje samodzielny produkt lub venture, stosujemy `SPIN_OUT`:

- nowa domena `PROJECT_MANAGED` przejmuje current product/project state,
- Lab zachowuje lineage i portfolio trail,
- current state nowej domeny nie jest dalej utrzymywany w Labie.

---

## 3. Project read plane — Google Drive

AI Mind `ROOT_FOLDER` i `SYNC_MANAGED` read mirror dla tej domeny:

https://drive.google.com/drive/folders/1h9VuzJb8ounJrjIGMrhxrSCC9yRdHCix

Workflow publikuje tutaj wyłącznie:

- `PROJECT_INDEX.md`,
- `docs/`,
- `state/`.

### `docs/`

Generowane projekcje trwałej wiedzy Labu, obecnie:

- `docs/lab-constitution.md`

### `state/`

Generowane projekcje current opportunity portfolio state:

- `state/signals.csv`
- `state/opportunities.csv`
- `state/hypotheses.csv`
- `state/experiments.csv`
- `state/evidence.csv`
- `state/decisions.csv`
- `state/operational-state.md`

Czytaj wyłącznie pliki potrzebne do bieżącego zadania. Nie rekonstruuj current state z pamięci rozmów, jeżeli dostępna jest aktualna projekcja.

Folder Drive jest `SYNC_MANAGED`. Nie zapisuj w nim ręcznie trwałych plików project knowledge/state ani nie poprawiaj ręcznie projekcji wygenerowanych przez workflow.

---

## 4. Project knowledge i opportunity portfolio state — Notion write plane

Canonical writable upstream dla durable knowledge i opportunity portfolio state:

- Workspace: `Nowe biznesy`
- Project root: `ZHC Lab OTECH`
- Project root ID: `3de66089-2751-80b0-832e-df92bc697eea`
- URL: https://app.notion.com/p/3de66089275180b0832edf92bc697eea

Managed objects pod rootem obejmują w szczególności:

- `Konstytucja Labu`,
- `Stan operacyjny`,
- `Dane/Signals`,
- `Dane/Opportunities`,
- `Dane/Hipotezy`,
- `Dane/Eksperymenty`,
- `Dane/Evidence`,
- `Dane/Decision Log`.

Dla trwałej zmiany knowledge/state przejdź do właściwego istniejącego managed object i wykonaj bounded mutation. Nie używaj Notion podczas zwykłego odczytu, jeśli aktualna projekcja Drive wystarcza.

Techniczne mapowanie managed Notion objects do projekcji utrzymuje `config/project.sources.yaml`. Stabilnych Notion IDs nie duplikujemy w tym Indexie poza rootem.

---

## 5. Execution — Linear i handoff

Authoritative owner dla backlogu, tasks, implementation work i execution status **Labu** jest Linear po zainstancjonowaniu właściwego projektu/workspace ZHC Lab OTECH.

Nie twórz równoległego backlogu w Notion, Drive, `state/` ani pamięci rozmowy. Notion może przechowywać metodologiczny/opportunity state i `next_decisive_action`, ale wykonywalne zadania i ich status należą do Linear.

Po handoffie do regularnej realizacji w OTECH wykonanie przestaje być current execution state Labu. Wtedy przejdź do domeny `OTECH` i zastosuj jej lokalny kontrakt/runtime.

---

## 6. Repo-native work — GitHub

GitHub `kriswpl/zhc-lab-otech` jest authoritative write ownerem dla:

- `PROJECT_INDEX.md`,
- `config/project.sources.yaml`,
- workflowów,
- skryptów synchronizacji,
- repo-native configuration i kodu.

`docs/` i `state/` w repozytorium są generowanymi/versioned projekcjami upstream Notion. Nie edytuj ich jako sposobu semantic write.

---

## 7. Routing według zadania

### Current opportunity portfolio state

`PROJECT_INDEX.md -> Drive state/ -> tylko potrzebny plik`

### Trwała wiedza Labu

`PROJECT_INDEX.md -> Drive docs/ -> tylko potrzebny dokument`

### Trwały semantic write do knowledge/state

`PROJECT_INDEX.md -> Notion ZHC Lab OTECH -> istniejący managed object -> bounded mutation`

### Execution / backlog / task status Labu

`PROJECT_INDEX.md -> Linear`

### Bieżący governance / reporting / financing / operational state spółki OTECH

`PROJECT_INDEX.md -> handoff do DOMAIN_KEY=OTECH -> lokalny entrypoint domeny OTECH`

Nie wyciągaj company-level current state OTECH z tego Labu.

### Kod / config / workflow / synchronizacja / PROJECT_INDEX

`PROJECT_INDEX.md -> GitHub kriswpl/zhc-lab-otech`

### Shared metoda Opportunity / Five Lenses / portfolio / evidence oraz source contract

`PROJECT_INDEX.md -> ZHC Product Base FLAT -> _ROOT.md -> właściwy dokument`

Dla project source/read/write/mutation rules:

`ZHC Product Base FLAT -> ZHC OS Engineering.md -> Project Source / Access / Mutation Contract`

Nie preloaduj wszystkich źródeł.

---

## 8. Sync, freshness i conflicts

- Notion -> GitHub/Drive dla project knowledge/state może mieć krótkie opóźnienie synchronizacji.
- Właśnie wykonany successful write do Notion nie może zostać cofnięty tylko dlatego, że Drive/GitHub pokazuje jeszcze starszą projekcję.
- Brakująca lub pusta projekcja jest ograniczeniem do zgłoszenia, nie pozwoleniem na rekonstrukcję current state z pamięci.
- Lab-specific opportunity state ma pierwszeństwo przed shared ZHC operating knowledge przy opisywaniu bieżącego stanu ZHC Lab OTECH.
- Domena `OTECH` ma pierwszeństwo przy claimach o bieżącym governance i operational state spółki.
- Po `SPIN_OUT` child domain jest authoritative dla nowego current product/project state; Lab zachowuje tylko lineage i własny portfolio trail.
- Konflikty rozwiązuj według klasy informacji i authoritative write ownera z sekcji 1 oraz shared ZHC contractu.

---

## 9. Runtime adapters

Adapter lub connector określa **jak** uzyskać dostęp do źródła, a nie **które źródło jest authoritative**.

Jeżeli wymagany source nie jest dostępny w danym runtime:

- nie zastępuj go innym source plane tylko dlatego, że jest dostępny,
- nie zapisuj semantic change do projekcji,
- wskaż brak dostępu lub pozostaw zmianę staged do wykonania przez właściwy write plane.

Nie zakładaj istnienia ZHC Skill, dopóki nie zostanie faktycznie wdrożony i jawnie wskazany jako aktywny runtime adapter.

---

## 10. Local overrides

`LOCAL_OVERRIDES: none`

Granica między `ZHC_LAB_OTECH` a `OTECH` jest lokalną regułą ownership/handoff, a nie odstępstwem od shared `Project Source / Access / Mutation Contract`.

---

## 11. Minimal repository / mirror structure

```text
ZHC Lab OTECH/
├── PROJECT_INDEX.md
├── config/
│   └── project.sources.yaml
├── scripts/
│   ├── sync-project-context.py
│   └── publish-project-context-to-drive.sh
├── .github/
│   └── workflows/
│       └── sync-project-context.yml
├── docs/                  # generated from Notion
│   └── lab-constitution.md
└── state/                 # generated from Notion
    ├── signals.csv
    ├── opportunities.csv
    ├── hypotheses.csv
    ├── experiments.csv
    ├── evidence.csv
    ├── decisions.csv
    └── operational-state.md
```

`PROJECT_INDEX.md` jest routerem. Semantic structures powstają w Notion. `docs/` i `state/` w GitHub oraz cały read mirror na Drive powstają przez workflow synchronizacji, nie przez ręczne edycje.
