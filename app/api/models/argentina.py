from typing import List
from pydantic import BaseModel

class Argentina(BaseModel):
    id: int
    name: str
    description: str
    stateCapital: str
    surface: int
    population: int
    languages: List[str]
    timeZone: str
    currency: str
    currencyCode: str
    currencySymbol: str
    isoCode: str
    internetDomain: str
    phonePrefix: str
    radioPrefix: str
    aircraftPrefix: str
    subRegion: str
    region: str
    borders: List[str]
    flags: List[str]

