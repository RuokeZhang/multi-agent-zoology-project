```python
import typing as t

# Minimal curated zoology knowledge base (expand as needed)
SPECIES_DATA: t.Dict[str, t.Dict[str, t.Any]] = {
    "african elephant": {
        "taxonomy": "Mammalia > Proboscidea > Elephantidae > Loxodonta africana",
        "habitat": "Savannas, grasslands, and forests across sub-Saharan Africa.",
        "range": "Sub-Saharan Africa",
        "environment": "Requires abundant water and access to vegetation.",
        "conservation": "Vulnerable (IUCN)",
        "threats": ["Habitat loss", "Poaching for ivory", "Human-wildlife conflict"],
        "protection": ["Anti-poaching patrols", "Habitat corridors", "CITES Appendix I"],
    },
    "giant panda": {
        "taxonomy": "Mammalia > Carnivora > Ursidae > Ailuropoda melanoleuca",
        "habitat": "Temperate broadleaf and mixed forests with dense bamboo understories.",
        "range": "South-central China (Sichuan, Shaanxi, Gansu)",
        "environment": "Cool, moist montane forests; relies on bamboo.",
        "conservation": "Vulnerable (IUCN)",
        "threats": ["Habitat fragmentation", "Low reproductive rate"],
        "protection": ["Protected reserves", "Bamboo habitat restoration", "Captive breeding"],
    },
    "emperor penguin": {
        "taxonomy": "Aves > Sphenisciformes > Spheniscidae > Aptenodytes forsteri",
        "habitat": "Antarctic sea ice and surrounding ocean.",
        "range": "Circumpolar Antarctica",
        "environment": "Cold marine environments; dependent on stable sea ice.",
        "conservation": "Near Threatened (IUCN)",
        "threats": ["Climate change", "Sea ice loss"],
        "protection": ["Marine protected areas", "Climate mitigation efforts"],
    },
}
```
