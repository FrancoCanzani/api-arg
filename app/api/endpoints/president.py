from fastapi import APIRouter, HTTPException
from app.utils.json_parser import parse_json
from datetime import datetime
from app.utils.unidecode_parser import remove_accents
from app.api.models.president import President
from typing import List

router = APIRouter(
    prefix="/api/v1/President",
    tags=["President"],
    responses={404: {"description": "Not found"}},
)

president_data = parse_json("app/data/president.json")


@router.get("/")
def get_presidents() -> List[President]:
    return president_data

@router.get("/id/{president_id}")
def get_president_by_id(president_id: int) -> President:
    filtered_presidents = [president for president in president_data if president["id"] == president_id]
    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")
    return filtered_presidents[0]

@router.get("/name/{president_name}")
def get_president_by_name(president_name: str) -> List[President]:
    president_name_lower = president_name.lower()
    president_name_no_accents = remove_accents(president_name_lower)
    filtered_presidents = [
        president
        for president in president_data
        if president_name_lower in president["name"].lower()
        or president_name_no_accents in remove_accents(president["name"]).lower()
        or president_name_lower in president["lastName"].lower()
        or president_name_no_accents in remove_accents(president["lastName"]).lower()
    ]
    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")
    return filtered_presidents

@router.get("/year/{period_year}")
def get_president_by_year(period_year: str) -> List[President]:
    filtered_presidents = []
    for president in president_data:
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

@router.get("/search/{keyword}")
def get_president_by_keyword(keyword: str) -> List[President]:
    keyword_lower = keyword.lower()
    keyword_no_accents = remove_accents(keyword_lower)
    filtered_presidents = [
        president
        for president in president_data
        if keyword_lower in president["name"].lower()
        or keyword_no_accents in remove_accents(president["name"]).lower()
        or keyword_lower in president["lastName"].lower()
        or keyword_no_accents in remove_accents(president["lastName"]).lower()
        or keyword_lower in president["politicalParty"].lower()
        or keyword_no_accents in remove_accents(president["politicalParty"]).lower()
        or keyword_lower in president["description"].lower()
        or keyword_no_accents in remove_accents(president["description"]).lower()
    ]
    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")
    return filtered_presidents

# Todo: add pagination for president list