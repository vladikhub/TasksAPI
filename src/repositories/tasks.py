from fastapi import HTTPException
from sqlalchemy import select, insert, delete, update, func, or_

from src.models.tasks import TasksModel
from src.schemas.tasks import Task, TaskAdd, TaskPatch


class TaskRepository:
    def __init__(self, session):
        self.session = session

    async def get_all(self, name) -> list[Task]:
        query = select(TasksModel).order_by(TasksModel.id)
        if name:
            query = query.filter(or_(
                func.lower(TasksModel.name).contains(name.strip().lower()),
                func.lower(TasksModel.description).contains(name.strip().lower())
            ))
        res = await self.session.execute(query)
        return [Task.model_validate(task, from_attributes=True) for task in res.scalars().all()]

    async def get_one_or_none(self, **filter_by) -> Task | None:
        query = select(TasksModel).filter_by(**filter_by)
        res = await self.session.execute(query)
        object = res.scalars().one_or_none()
        if object is None:
            return None
        return Task.model_validate(object, from_attributes=True)

    async def create(self, data: TaskAdd) -> Task:
        add_task_stmt = insert(TasksModel).values(**data.model_dump()).returning(TasksModel)
        res = await self.session.execute(add_task_stmt)
        task = res.scalars().one()
        return Task.model_validate(task, from_attributes=True)

    async def delete(self, task_id: int):
        query = select(TasksModel).filter_by(id=task_id)
        res = await self.session.execute(query)
        object = res.scalars().one_or_none()
        if object is None:
            raise HTTPException(status_code=404, detail="Таски с таким id не существует")
        delete_task_stmt = delete(TasksModel).filter_by(id=task_id)
        await self.session.execute(delete_task_stmt)

    async def update(self, task_id: int, exclude_unset: bool, data: TaskPatch):
        query = select(TasksModel).filter_by(id=task_id)
        res = await self.session.execute(query)
        task = res.scalars().one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Таски с таким id не существует")
        update_task_stmt = update(TasksModel).filter_by(id=task_id).values(**data.model_dump(exclude_unset=exclude_unset)).returning(TasksModel)
        res = await self.session.execute(update_task_stmt)
        model = res.scalars().one()
        return Task.model_validate(model, from_attributes=True)


