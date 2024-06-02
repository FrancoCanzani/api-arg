from fastapi import APIRouter
from app.utils.json_parser import parse_json
from app.api.models.argentina import Argentina

router = APIRouter(
    prefix="/api/v1/argentina",
    tags=["Argentina"],
    responses={404: {"description": "Not found"}},
)

argentina_data = parse_json("app/data/argentina.json")

print(argentina_data)

@router.get("/")
def get_argentina() -> Argentina:
    return argentina_data[0]
