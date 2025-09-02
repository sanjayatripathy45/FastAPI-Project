#src.db.main.py

from sqlmodel import create_engine, text,SQLModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
# from src.models import Book
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator

from src.config import Config

# engine = AsyncEngine(
#     create_engine(
#     url= Config.DATABASE_URL,
#     echo = True,
#     connect_args={"statement_cache_size": 0}
# ))

async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL,echo=True,
    connect_args={"statement_cache_size": 0}))


# For Reference 
# engine = create_async_engine(
#     Config.DATABASE_URL,
#     echo=True,
# )

async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with Session() as session:
        yield session