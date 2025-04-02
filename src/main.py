import sys
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI



sys.path.append(str(Path(__file__).parent.parent))

from src.routers.tasks import router as tasks_router
from src.database import create_tables



# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     run_migrations()
#     print("Миграции применены")
#     yield


app = FastAPI()

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

