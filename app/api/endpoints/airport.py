from fastapi import APIRouter, HTTPException, Query
from app.utils.json_parser import parse_json
from app.utils.unidecode_parser import remove_accents
from app.api.models.airport import Airport
from typing import List

router = APIRouter(
    prefix="/api/v1/airport",
    tags=["Airport"],
    responses={404: {"description": "Not found"}},
)

airport_data = parse_json("app/data/airport.json")


@router.get("/")
def get_airports() -> List[Airport]:
    return airport_data


@router.get("/id/{airport_id}")
def get_airport_by_id(airport_id: int) -> Airport:
    for airport in airport_data:
        if airport["id"] == airport_id:
            return airport
    raise HTTPException(status_code=404, detail="Airport not found")


@router.get("/name/{airport_name}")
def get_airport_by_name(airport_name: str) -> List[Airport]:
    airport_name_lower = airport_name.lower()
    airport_name_no_accents = remove_accents(airport_name_lower)
    filtered_airports = [
        airport
        for airport in airport_data
        if airport_name_lower in airport["name"].lower()
        or airport_name_no_accents in remove_accents(airport["name"]).lower()
    ]

    if not filtered_airports:
        raise HTTPException(status_code=404, detail="Airport not found")

    return filtered_airports


@router.get("/city/{airport_city}")
def get_airport_by_city(airport_city: str) -> List[Airport]:
    airport_city_lower = airport_city.lower()
    airport_city_no_accents = remove_accents(airport_city_lower)
    filtered_airports = [
        airport
        for airport in airport_data
        if airport_city_lower in airport["city"].lower()
        or airport_city_no_accents in remove_accents(airport["city"]).lower()
    ]

    if not filtered_airports:
        raise HTTPException(status_code=404, detail="Airport not found")

    return filtered_airports


@router.get("/district/{airport_district}")
def get_airport_by_district(airport_district: str) -> List[Airport]:
    airport_district_lower = airport_district.lower()
    airport_district_no_accents = remove_accents(airport_district_lower)
    filtered_airports = [
        airport
        for airport in airport_data
        if airport_district_lower in airport["district"].lower()
        or airport_district_no_accents in remove_accents(airport["district"]).lower()
    ]

    if not filtered_airports:
        raise HTTPException(status_code=404, detail="Airport not found")

    return filtered_airports


@router.get("/code/{airport_code}")
def get_airport_by_code(airport_code: str) -> List[Airport]:
    airport_code_lower = airport_code.lower()
    filtered_airports = [
        airport
        for airport in airport_data
        if airport_code_lower in airport["oaci"].lower()
        or airport_code_lower in airport["iata"].lower()
        or airport_code_lower in airport["anac"].lower()
    ]

    if not filtered_airports:
        raise HTTPException(status_code=404, detail="Airport not found")

    return filtered_airports


# Todo: add pagination for airport list
