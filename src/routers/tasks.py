from fastapi import APIRouter, Body, Query

from src.database import async_session_maker
from src.schemas.tasks import TaskAdd, Task, TaskPatch
from src.repositories.tasks import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Таски"])

@router.get("", summary="Получить таски",)
async def get_tasks(
        name: str | None = Query(default=None, description="Название таски")
) -> list[Task]:
    async with async_session_maker() as session:
        tasks = await TaskRepository(session).get_all(name=name)
    return tasks

@router.get("/{task_id}", summary="Получить таску по id",)
async def get_task_by_id(task_id: int) -> Task | None:
    async with async_session_maker() as session:
        task = await TaskRepository(session).get_one_or_none(id=task_id)
    return task

@router.post("", summary="Добавить новую таску")
async def create_task(data: TaskAdd = Body(openapi_examples={
    "1": {"summary": "Фотосеcсия", "value": {
        "name": "Фотосеcсия",
        "description": "Одеться красиво",
        "is_active": 1
    }},
    "2": {"summary": "Проект", "value": {
        "name": "Проект",
        "description": "Сделать одну задачу",
        "is_active": 1
    }},
})):
    async with async_session_maker() as session:
        task = await TaskRepository(session).create(data)
        await session.commit()
    return {"task": Task.model_validate(task, from_attributes=True)}


@router.patch("/update_some/{task_id}", summary="Изменить какие-то поля таски")
async def update_task_some_fields(
        task_id: int,
        data: TaskPatch = Body()
):
    async with async_session_maker() as session:
        task = await TaskRepository(session).update(task_id, True, data)
        await session.commit()
    return task

@router.put("/update_all/{task_id}", summary="Изменить все поля таски")
async def update_task_all_fields(
        task_id: int,
        data: TaskPatch = Body(openapi_examples={
            "1": {"summary": "Фотосеcсия", "value": {
                "name": "Фотосеcсия",
                "description": "Одеться красиво",
                "is_active": 1
            }},
            "2": {"summary": "Проект", "value": {
                "name": "Проект",
                "description": "Сделать одну задачу",
                "is_active": 1
            }},
})):
    async with async_session_maker() as session:
        task = await TaskRepository(session).update(task_id, False, data)
        await session.commit()
    return task


@router.delete("/delete/{task_id}", summary="Удалить таску")
async def delete_task(task_id: int):
    async with async_session_maker() as session:
        await TaskRepository(session).delete(task_id)
        await session.commit()
    return {"status": "OK"}

