from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json

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
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_districts[0]
