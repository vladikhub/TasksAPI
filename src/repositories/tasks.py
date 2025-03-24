from sqlalchemy import select, insert, delete

from src.models.tasks import TasksModel
from src.schemas.tasks import Task, TaskAdd


class TaskRepository:
    def __init__(self, session):
        self.session = session

    async def get_tasks(self) -> list[Task]:
        query = select(TasksModel)
        res = await self.session.execute(query)
        return [Task.model_validate(task, from_attributes=True) for task in res.scalars().all()]

    async def create_task(self, data: TaskAdd) -> Task:
        add_task_stmt = insert(TasksModel).values(**data.model_dump()).returning(TasksModel)
        res = await self.session.execute(add_task_stmt)
        task = res.scalars().one()
        return Task.model_validate(task, from_attributes=True)

    async def delete_task(self, task_id: int):
        delete_task_stmt = delete(TasksModel).filter_by(id=task_id)
        await self.session.execute(delete_task_stmt)
