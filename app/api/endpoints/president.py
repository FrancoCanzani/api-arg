from fastapi import APIRouter, HTTPException, Depends
from app.utils.json_parser import parse_json
from datetime import datetime

router = APIRouter(
    prefix="/api/v1/President",
    tags=["President"],
    responses={404: {"description": "Not found"}},
)

presidentes_data = parse_json("app/data/presidentes.json")


@router.get("/")
def get_presidents():
    return presidentes_data

@router.get("/id/{president_id}")
def get_president_by_id(president_id: int):
    filtered_presidents = [
        president for president in presidentes_data if president["id"] == president_id
    ]

    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_presidents[0]

@router.get("/name/{president_name}")
def get_president_by_name(president_name: str):
    filtered_presidents = [
        president
        for president in presidentes_data
        if str(president_name).lower() in president["name"].lower()
        or str(president_name).lower() in president["lastName"].lower()
    ]

    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_presidents

@router.get("/year/{period_year}")
def get_president_by_year(period_year: str):
    filtered_presidents = []

    for president in presidentes_data:
        start_year = int(president["startPeriodDate"][:4])
        end_year = None

        if president["endPeriodDate"].lower() == "presente":
            end_year = datetime.now().year
        else:
            end_year = int(president["endPeriodDate"][:4])

        if (int(period_year) >= start_year) and (int(period_year) <= end_year):
            filtered_presidents.append(president)

    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_presidents