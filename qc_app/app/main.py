from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api import health
from app.db.database import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(health.router)

@app.get("/")
def home():
    return "Connected to FastAPI"