import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.routers.tasks import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

