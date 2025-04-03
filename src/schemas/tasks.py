import datetime


from pydantic import BaseModel, Field


class TaskAdd(BaseModel):
    name: str
    description: str
    is_active: bool


class Task(TaskAdd):
    id: int
    created_at: datetime.datetime


class TaskPatch(BaseModel):
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)