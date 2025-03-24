from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.api.tasks import router as tasks_router
from src.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Таблица создана")
    yield
    print("Закончили")

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)

