
from fastapi import FastAPI, Header, status, APIRouter, Depends
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.books.schemas import Book, BookUpdateModel, BookCreateModel,BooksResponse
from src.books.book_data import books
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService


# New Book API 
book_router = APIRouter()

book_service = BookService()

@book_router.get("/", response_model=BooksResponse)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)

    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED) 
async def create_a_books(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return new_book



@book_router.get("/{book_uid}")
async def get_book(book_uid: int, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_uid, session)

    if book is not None: 
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details= "Book Not found")
        

@book_router.patch("/{book_uid}")
async def update_a_books(book_uid: int, update_data: BookUpdateModel, session: AsyncSession = Depends(get_session)):
    book = await book_service.update_book(book_uid, update_data, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_books(book_uid: int, session: AsyncSession = Depends(get_session)):
    book_delete = await book_service.delete_book(book_uid,session )

    if book_delete:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")





# @book_router.get("/{book_id}")
# async def get_book(book_id: int) -> dict:
#     for book in books:
#         if(book['id'] == book_id):
#             return book
        
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details= "Book Not found")
        



# @book_router.patch("/{book_id}")
# async def update_a_books(book_id: int, update_data: BookUpdateModel) -> dict:
#     for book in books:
#         if book["id"] == book_id:
#             book['title'] = update_data.title
#             book["author"]= update_data.author
#             book["publisher"] = update_data.publisher
#             book['language'] = update_data.language
#             book['page_count'] = update_data.page_count

#             return book
        
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")



# @book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_a_books(book_id: int):
#     for book in books:
#         if book['id'] == book_id:
#             books.remove(book)

#             return {}
        
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")

