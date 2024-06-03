from fastapi import APIRouter
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
    return tourism_data


# uvicorn app.main:app --reload --reload-exclude '*.json'