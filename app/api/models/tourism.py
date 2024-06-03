from pydantic import BaseModel
from typing import List, Dict

class EntryMethods(BaseModel):
    air: float
    sea: float
    land: float

class Travels(BaseModel):
    total: float
    entryMethods: EntryMethods

class MonthlyData(BaseModel):
    visitorsTravels: Travels
    touristsTravels: Travels
    excursionistsTravels: Travels
    visitors: Travels
    tourists: Travels
    excursionists: Travels

class Tourism(BaseModel):
    id: int
    month: str
    data: MonthlyData
