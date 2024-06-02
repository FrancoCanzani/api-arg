from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json
from app.utils.unidecode_parser import remove_accents
from app.api.models.department import Department
from typing import List, Optional

router = APIRouter(
    prefix="/api/v1/department",
    tags=["Department"],
    responses={404: {"description": "Not found"}},
)

department_data = parse_json("app/data/department.json")


@router.get("/")
def get_departments() -> List[Department]:
    return department_data


@router.get("/id/{department_id}")
def get_department_by_id(department_id: int) -> Department:
    for department in department_data:
        if department["id"] == department_id:
            return department
    raise HTTPException(status_code=404, detail="Department not found")


@router.get("/name/{department_name}")
def get_department_by_name(department_name: str) -> List[Department]:
    department_name_lower = department_name.lower()
    department_name_no_accents = remove_accents(department_name_lower)
    filtered_departments = [
        department
        for department in department_data
        if department_name_lower in department["name"].lower()
        or department_name_no_accents in remove_accents(department["name"]).lower()
    ]

    if not filtered_departments:
        raise HTTPException(status_code=404, detail="Department not found")

    return filtered_departments


@router.get("/district/name/{district_name}")
def get_department_by_district_name(district_name: str) -> List[Department]:
    department_district_lower = district_name.lower()
    department_district_no_accents = remove_accents(department_district_lower)
    filtered_departments = [
        department
        for department in department_data
        if department_district_lower in department["district"]["name"].lower()
        or department_district_no_accents
        in remove_accents(department["district"]["name"]).lower()
    ]

    if not filtered_departments:
        raise HTTPException(status_code=404, detail="Department not found")

    return filtered_departments


@router.get("/district/id/{district_id}")
def get_department_by_district_id(district_id: int) -> Department:
    for department in department_data:
        if department["district"]["id"] == district_id:
            return department
    raise HTTPException(status_code=404, detail="Department not found")


# Todo: add pagination for department list
