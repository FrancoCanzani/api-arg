from fastapi import FastAPI
from app.api.endpoints import president, argentina, district, airport, department, tourism

app = FastAPI(title="Api-Argentina")


@app.get("/")
def root():
    return "Hello world!"


app.include_router(president.router)
app.include_router(argentina.router)
app.include_router(district.router)
app.include_router(airport.router)
app.include_router(department.router)
app.include_router(tourism.router)

# uvicorn app.main:app --reload --reload-exclude '*.json'