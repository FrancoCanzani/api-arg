from fastapi import FastAPI
from app.api.endpoints import president, argentina

app = FastAPI(title='Api-Argentina')


@app.get("/")
async def root():
    return "Hello world!"

app.include_router(president.router)
app.include_router(argentina.router)