from fastapi import FastAPI
from utils.json_parser import parse_json

app = FastAPI()

version = "v1"

@app.get(f"/api/{version}")
async def read_users():
    return "Hello world!"

@app.get(f"/api/{version}/Argentina")
def argentina():
    argentina_data = parse_json('data/argentina.json')
    return argentina_data

@app.get(f"/api/{version}/President")
def argentina():
    presidentes_data = parse_json('data/presidentes.json')
    return presidentes_data
