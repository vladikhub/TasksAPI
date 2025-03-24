from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine = create_async_engine(settings.DB_URL)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


session = async_session_maker()

class Base(DeclarativeBase):
    pass


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
