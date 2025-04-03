import datetime


from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class TasksModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str]
    is_active: Mapped[bool]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
