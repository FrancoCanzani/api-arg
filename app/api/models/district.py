from pydantic import BaseModel, Field
from typing import Optional

class Centroid(BaseModel):
    lon: float = Field(..., description="Longitude of the centroid")
    lat: float = Field(..., description="Latitude of the centroid")

class District(BaseModel):
    id: int
    flag: str
    name: str
    capital: Optional[str]
    population: int
    surface: int
    category: str
    centroid: Centroid
    iso_id: str
    description: str
