from fastapi import FastAPI, HTTPException
from utils.json_parser import parse_json

app = FastAPI()


@app.get(f"/api/v1")
async def read_users():
    return "Hello world!"


@app.get(f"/api/v1/Argentina")
def argentina():
    argentina_data = parse_json("data/argentina.json")
    return argentina_data


@app.get(f"/api/v1/President")
def argentina():
    presidentes_data = parse_json("data/presidentes.json")
    return presidentes_data


@app.get("/api/v1/President/id/{president_id}")
def argentina(president_id: int):
    presidentes_data = parse_json("data/presidentes.json")
    filtered_presidents = [
        president for president in presidentes_data if president["id"] == president_id
    ]

    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_presidents


@app.get("/api/v1/President/name/{president_name}")
def argentina(president_name: str):
    presidentes_data = parse_json("data/presidentes.json")
    filtered_presidents = [
        president
        for president in presidentes_data
        if str(president_name).lower() in president["name"].lower()
        or str(president_name).lower() in president["lastName"].lower()
    ]

    if not filtered_presidents:
        raise HTTPException(status_code=404, detail="President not found")

    return filtered_presidents
