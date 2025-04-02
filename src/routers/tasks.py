from fastapi import APIRouter, Body, Query

from src.database import async_session_maker
from src.schemas.tasks import TaskAdd, Task
from src.repositories.tasks import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Таски"])

@router.get("", summary="Получить все таски",)
async def get_tasks() -> list[Task]:
    async with async_session_maker() as session:
        tasks = await TaskRepository(session).get_tasks()
    return tasks

@router.post("", summary="Добавить новую таску")
async def create_task(data: TaskAdd = Body(openapi_examples={
    "1": {"summary": "Фотосеcсия", "value": {
        "name": "Фотосеcсия",
        "description": "Одеться красиво"
    }},
    "2": {"summary": "Проект", "value": {
        "name": "Проект",
        "description": "Сделать одну задачу"
    }},
})):
    async with async_session_maker() as session:
        task = await TaskRepository(session).create_task(data)
        await session.commit()
    return {"task": Task.model_validate(task, from_attributes=True)}

@router.delete("")
async def delete_task(task_id: int = Query()):
    async with async_session_maker() as session:
        await TaskRepository(session).delete_task(task_id)
        await session.commit()
    return {"status": "OK"}
