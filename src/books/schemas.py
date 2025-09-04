from pydantic import BaseModel
from typing import List
from datetime import datetime, date
import uuid

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    language: str
    publisher: str
    page_count: int
    publisher_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class BookResponse(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    publisher_date: date
    language: str
    page_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class BooksResponse(BaseModel):
    message: str
    status: int
    data: List[BookResponse]

class BookCreateModel(BaseModel):
    title: str
    author: str
    language: str
    publisher: str
    page_count: int
    publisher_date: date


class BookUpdateModel(BaseModel):
    title: str
    author: str
    language: str
    publisher: str
    page_count: int