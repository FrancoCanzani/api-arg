from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json
from app.utils.unidecode_parser import remove_accents

router = APIRouter(
    prefix="/api/v1/District",
    tags=["District"],
    responses={404: {"description": "Not found"}},
)

district_data = parse_json("app/data/district.json")


@router.get("/")
def get_district():
    return district_data


@router.get("/id/{district_id}")
def get_president_by_id(district_id: int):
    filtered_districts = [
        district for district in district_data if district["id"] == district_id
    ]

    if not filtered_districts:
        raise HTTPException(status_code=404, detail="District not found")

    return filtered_districts[0]


@router.get("/name/{district_name}")
def get_district_by_name(district_name: str):
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
def get_district_by_capital(district_capital: str):
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