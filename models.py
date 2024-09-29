from pydantic import BaseModel
from typing import List, Optional

# Modelos de planta
class PlantBase(BaseModel):
    name: str
    origin: str
    habitat: str
    light: str
    temperature: str
    altitude: Optional[int]

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    pass

class Plant(PlantBase):
    id: int
    pests: List[str]  # Lista de códigos de plagas
    nutrients: List[str]  # Lista de códigos de nutrientes

# Modelos de plaga
class Pest(BaseModel):
    code: str
    name: str
    description: str
    harmful_plants: List[str]  # Lista de plantas afectadas

# Modelos de nutrientes
class Nutrient(BaseModel):
    code: str
    name: str
    description: str
    essential_plants: List[str]  # Lista de plantas que requieren este nutriente
