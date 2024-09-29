from fastapi import FastAPI, HTTPException
from typing import List
from models import Plant, PlantCreate, PlantUpdate, Pest, Nutrient
from database import plants_db, pests_db, nutrients_db

app = FastAPI()

# Listar todas las plantas
@app.get("/plants", response_model=List[Plant])
def get_plants():
    return plants_db

# Obtener una planta por su ID
@app.get("/plants/{plant_id}", response_model=Plant)
def get_plant(plant_id: int):
    for plant in plants_db:
        if plant.id == plant_id:
            return plant
    raise HTTPException(status_code=404, detail="Plant not found")

# Crear una nueva planta
@app.post("/plants", response_model=Plant)
def create_plant(plant: PlantCreate):
    new_plant = Plant(id=len(plants_db) + 1, **plant.dict())
    plants_db.append(new_plant)
    return new_plant

# Actualizar una planta
@app.put("/plants/{plant_id}", response_model=Plant)
def update_plant(plant_id: int, plant: PlantUpdate):
    for i, p in enumerate(plants_db):
        if p.id == plant_id:
            updated_plant = Plant(id=plant_id, **plant.dict())
            plants_db[i] = updated_plant
            return updated_plant
    raise HTTPException(status_code=404, detail="Plant not found")

# Eliminar una planta
@app.delete("/plants/{plant_id}")
def delete_plant(plant_id: int):
    for i, plant in enumerate(plants_db):
        if plant.id == plant_id:
            del plants_db[i]
            return {"detail": "Plant deleted"}
    raise HTTPException(status_code=404, detail="Plant not found")

# Listar todas las plagas
@app.get("/pests", response_model=List[Pest])
def get_pests():
    return pests_db

# Obtener una plaga por su código
@app.get("/pests/{pest_code}", response_model=Pest)
def get_pest(pest_code: str):
    for pest in pests_db:
        if pest.code == pest_code:
            return pest
    raise HTTPException(status_code=404, detail="Pest not found")

# Listar todos los nutrientes
@app.get("/nutrients", response_model=List[Nutrient])
def get_nutrients():
    return nutrients_db

# Obtener un nutriente por su código
@app.get("/nutrients/{nutrient_code}", response_model=Nutrient)
def get_nutrient(nutrient_code: str):
    for nutrient in nutrients_db:
        if nutrient.code == nutrient_code:
            return nutrient
    raise HTTPException(status_code=404, detail="Nutrient not found")
