from pydantic import BaseModel
from typing import Literal

class Airport(BaseModel):
    id: int
    city: str
    district: str
    oaci: str
    iata: str
    anac: str
    name: str
    districtId: int
    type: Literal["nacional", "internacional"] 
    totalPassengers2023: int
