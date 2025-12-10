```python
from typing import Dict, Any
from .knowledge_base import SPECIES_DATA

class SpeciesClassifierAgent:
    def answer(self, species_query: str) -> Dict[str, Any]:
        species = species_query.lower()
        data = SPECIES_DATA.get(species)
        # TODO: Add fuzzy matching / semantic lookup for species names
        if not data:
            return {"agent": "SpeciesClassifierAgent", "error": "Species not found", "query": species_query}
        return {
            "agent": "SpeciesClassifierAgent",
            "taxonomy": data.get("taxonomy"),
            "notes": f"{species_query.title()} belongs to {data.get('taxonomy')}",
        }

class HabitatAnalystAgent:
    def answer(self, species_query: str) -> Dict[str, Any]:
        species = species_query.lower()
        data = SPECIES_DATA.get(species)
        # TODO: Add richer habitat reasoning and environmental parameter outputs
        if not data:
            return {"agent": "HabitatAnalystAgent", "error": "Species not found", "query": species_query}
        return {
            "agent": "HabitatAnalystAgent",
            "habitat": data.get("habitat"),
            "range": data.get("range"),
            "environment": data.get("environment"),
        }

class ConservationAdvisorAgent:
    def answer(self, species_query: str) -> Dict[str, Any]:
        species = species_query.lower()
        data = SPECIES_DATA.get(species)
        # TODO: Integrate real conservation databases (e.g., IUCN API)
        if not data:
            return {"agent": "ConservationAdvisorAgent", "error": "Species not found", "query": species_query}
        return {
            "agent": "ConservationAdvisorAgent",
            "status": data.get("conservation"),
            "threats": data.get("threats"),
            "protection": data.get("protection"),
        }

class Planner:
    def __init__(self):
        self.species_agent = SpeciesClassifierAgent()
        self.habitat_agent = HabitatAnalystAgent()
        self.conservation_agent = ConservationAdvisorAgent()

    def route(self, agent_name: str, species_query: str) -> Dict[str, Any]:
        # TODO: Add smarter routing / multi-agent coordination with shared context
        if agent_name == "classifier":
            return self.species_agent.answer(species_query)
        if agent_name == "habitat":
            return self.habitat_agent.answer(species_query)
        if agent_name == "conservation":
            return self.conservation_agent.answer(species_query)
        return {"error": "Unknown agent", "agent": agent_name}
```
