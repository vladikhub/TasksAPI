from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class TasksModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str]