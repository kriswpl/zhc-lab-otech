<!-- GENERATED FROM NOTION. DO NOT EDIT MANUALLY. -->
<!-- notion-page-id: 3de66089275181f49d9dcc63e569f4eb -->

# Konstytucja Labu

## Rola domeny

`ZHC_LAB_OTECH` jest project-managed Opportunity Labem dla eksperymentów i Opportunities ZHC związanych z OTECH.

Lab służy do intake sygnałów, discovery, walidacji, eksperymentów i decyzji portfelowych przed przejściem do wykonywalnej pracy.

## Ownership

Lab owns:

- Signals dotyczące możliwych nowych produktów, usług, modeli biznesowych i zmian testowanych metodą ZHC w kontekście OTECH.

- Opportunities i ich stage / portfolio decision.

- Hipotezy, eksperymenty, evidence oraz decyzje eksperymentalne.

- Lineage od sygnału do decyzji o dalszym losie Opportunity.

Lab **nie owns** bieżącego governance, raportowania, finansowania, decyzji Rady Nadzorczej ani operacyjnego state spółki OTECH. Te informacje należą do domeny `OTECH`.

## Zasada handoff

Dopóki temat jest Opportunity / eksperymentem ZHC, current opportunity state pozostaje w `ZHC_LAB_OTECH`.

Gdy temat przechodzi do regularnej realizacji w OTECH, bieżący operational/execution state przejmuje domena `OTECH`; Lab zachowuje evidence i decision trail. Gdy powstaje samodzielny produkt lub venture, stosujemy `SPIN_OUT` do nowej domeny `PROJECT_MANAGED`.

## Shared method

Lab dziedziczy shared metodę ZHC dla Opportunity, portfolio, Five Lenses, evidence i eksperymentów. Shared metodologia nie jest kopiowana do tej domeny; lokalny router wskazuje ZHC Product Base jako read plane.

## Technical contract

`STATE_MODE = PROJECT_MANAGED`.

Semantic knowledge/state writes powstają w Notion. GitHub i Drive przechowują generowane projekcje. Execution tasks nie są duplikowane w Notion ani Drive i trafiają do authoritative execution plane wskazanego przez `PROJECT_INDEX.md`.
