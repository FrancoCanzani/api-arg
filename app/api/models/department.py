from pydantic import BaseModel, Field
from typing import Literal

class Centroid(BaseModel):
    lon: float = Field(..., description="Longitude of the centroid")
    lat: float = Field(..., description="Latitude of the centroid")

class District(BaseModel):
    id: int
    name: str
    intersection: float
    
    
class Department(BaseModel):
    id: int
    name: str
    fullName: str
    district: District
    category: Literal["comuna", "partido", "departamento"] 
    centroid: Centroid
