from pydantic import BaseModel


class TaskAdd(BaseModel):
    name: str
    description: str

class Task(TaskAdd):
    id: int

