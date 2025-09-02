from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid 

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default= uuid.uuid4
        )

    )
    title: str
    author: str
    publisher: str
    publisher_date: str
    language: str
    page_count: int
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.utcnow)
    )
    updated_at: datetime = Field(
    sa_column=Column(pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
)

def __repr__(self):
    return f"<Book {self.title}>"

