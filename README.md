# Zoology Multi-Agent Assistant

Multi-agent Flask app that helps students and citizen scientists explore species taxonomy, habitats, and conservation status. Three specialized agents are orchestrated by a simple Python planner, with a tabbed single-page UI to chat with each role.

## Quick Start

```bash
git clone <repo-url> zoology-agents
cd zoology-agents
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app.py run  # defaults to http://127.0.0.1:5000
```

- Data: a small curated zoology dataset lives in `data/species.json` (edit/extend as needed).
- Environment: no external APIs required; runs offline.

## Endpoints & UI

- `GET /` – Single-page UI with tabs for each agent (Species, Habitat, Conservation).
- `POST /api/classify` – SpeciesClassifierAgent: classify species and answer taxonomy questions.
- `POST /api/habitat` – HabitatAnalystAgent: habitat, range, environmental needs.
- `POST /api/conservation` – ConservationAdvisorAgent: conservation status, threats, protection notes.
- (Planner) – Internal: routes user intent to the appropriate agent(s); keeps responses scoped to their role.
- (Static) – Basic assets for tabs and optional icons in `static/`.

## Features

- Three specialized agents with non-overlapping prompts and a simple coordinator.
- Curated, small zoology knowledge base for reliable offline answers.
- Flask SPA with tabbed chats to view distinct agent responses.
- Educational disclaimer: not a substitute for expert or regulatory guidance.

## TODO

- [MUST] Implement multi-agent orchestration (planner + SpeciesClassifierAgent, HabitatAnalystAgent, ConservationAdvisorAgent).
- [MUST] Build SpeciesClassifierAgent against the curated zoology knowledge base.
- [MUST] Build HabitatAnalystAgent for habitats, ranges, and environmental needs.
- [MUST] Build ConservationAdvisorAgent for status, threats, and protection summaries.
- [MUST] Complete Flask single-page UI with tabs for each agent’s chat and responses.
- [OPTIONAL] Add a ZoologyAgent for hybrid keyword + semantic search over fact sheets/abstracts.
- [OPTIONAL] Add simple range maps or habitat icons in the UI (static/public-domain assets).
- [OPTIONAL] Support batch CSV upload for conservation risk summaries.
- [OPTIONAL] Add a developer console to inspect recent conversations, timing, and logs.
- [OPTIONAL] Add lightweight caching for repeated species questions.
