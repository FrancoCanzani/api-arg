from fastapi import FastAPI
import json

app = FastAPI()

def parse_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
@app.get("/")
async def read_users():
    return ["Rick", "Franco"]

@app.get("/api/v1/Argentina")
def argentina():
    argentina_data = parse_json('data/argentina.json')
    return argentina_data
