from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json
from app.utils.unidecode_parser import remove_accents
from app.api.models.district import District
from typing import List

router = APIRouter(
    prefix="/api/v1/district",
    tags=["District"],
    responses={404: {"description": "Not found"}},
)

district_data = parse_json("app/data/district.json")


@router.get("/")
def get_district() -> List[District]:
    return district_data


@router.get("/id/{district_id}")
def get_district_by_id(district_id: int) -> District:
    for district in district_data:
        if district["id"] == district_id:
            return district
        raise HTTPException(status_code=404, detail="District not found")


@router.get("/name/{district_name}")
def get_district_by_name(district_name: str) -> List[District]:
    district_name_lower = district_name.lower()
    district_name_no_accents = remove_accents(district_name_lower)
    filtered_districts = [
        district
        for district in district_data
        if district_name_lower in district["name"].lower()
        or district_name_no_accents in remove_accents(district["name"]).lower()
    ]

    if not filtered_districts:
        raise HTTPException(status_code=404, detail="District not found")

    return filtered_districts


@router.get("/capital/{district_capital}")
def get_district_by_capital(district_capital: str) -> List[District]:
    district_capital_lower = district_capital.lower()
    district_capital_no_accents = remove_accents(district_capital_lower)
    filtered_districts = [
        district
        for district in district_data
        if district_capital_lower in district["capital"].lower()
        or district_capital_no_accents in remove_accents(district["capital"]).lower()
    ]

    if not filtered_districts:
        raise HTTPException(status_code=404, detail="District not found")

    return filtered_districts
