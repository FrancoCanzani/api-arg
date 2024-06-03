from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json
from app.api.models.tourism import Tourism
from typing import List, Dict

router = APIRouter(
    prefix="/api/v1/tourism",
    tags=["Tourism"],
    responses={404: {"description": "Not found"}},
)

tourism_data = parse_json("app/data/tourism.json")


@router.get("/")
def get_tourism() -> List[Dict[str, List[Tourism]]]: 
    # This return type took me 6 hours
    
    return tourism_data


@router.get("/month/{month}")
def get_tourism_by_month(month: str) -> Tourism:
    data = tourism_data[0].get("2023")
    
    if not data:
        raise HTTPException(status_code=404, detail="Data for the year 2023 not found")
    
    month_lower = month.lower()
    
    for entry in data:
        if entry["month"].lower() == month_lower:
            return entry
    
    raise HTTPException(status_code=404, detail="Month not found")


