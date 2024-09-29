from models import Plant, Pest, Nutrient

# Base de datos simulada de plantas
plants_db = [
    Plant(id=1, name="Ficus", origin="Asia", habitat="Interior", light="Indirecta", temperature="20-30°C", altitude=None, pests=["P001"], nutrients=["N001"]),
    Plant(id=2, name="Cactus", origin="América", habitat="Desierto", light="Directa", temperature="20-40°C", altitude=500, pests=["P002"], nutrients=["N002"]),
]

# Base de datos simulada de plagas
pests_db = [
    Pest(code="P001", name="Ácaros", description="Plaga pequeña que afecta a las hojas.", harmful_plants=["Ficus"]),
    Pest(code="P002", name="Cochinilla", description="Plaga que succiona la savia de las plantas.", harmful_plants=["Cactus"]),
]

# Base de datos simulada de nutrientes
nutrients_db = [
    Nutrient(code="N001", name="Nitrógeno", description="Elemento esencial para el crecimiento de las hojas.", essential_plants=["Ficus"]),
    Nutrient(code="N002", name="Potasio", description="Fortalece el sistema inmunológico de las plantas.", essential_plants=["Cactus"]),
]
