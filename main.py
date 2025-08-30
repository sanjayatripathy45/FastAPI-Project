from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel



app = FastAPI()

# @app.get('/')
# async def read_root():
#     return {"message": "Hello World"}

# # Using Parameter
# @app.get('/greet/{name}')
# async def greet_name_by_params(name: str) -> dict:
#     return {"message": f"Hello {name}"}


# # Using Query parms
# @app.get('/greet')
# async def greet_name_by_query(name: str) -> dict:
#     return {"message": f"Hello {name}"}

# # Using Optional and Default Value to parameter
# @app.get("/greet-optional")
# async def greet_name_by_default_and_optional(name: Optional[str]="sanjaya", age: int = 0) -> dict:
#     return{"message": f"Hello { name}", "age": age}


# class BookCreateModel(BaseModel):
#     title: str
#     author: str

# @app.post('/create-book')
# async def create_book(book_data: BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }

# @app.get("/get_header", status_code=200)
# async def get_header(
#     accept: str = Header(None) ,
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_header = {}
#     request_header["Accept"] = accept
#     request_header['Content-Type'] = content_type
#     request_header["User-Agent"] = user_agent
#     request_header["Host"] = host


#     return request_header



# New Book API 

books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publisher_date": "1999-10-20",
        "publisher": "Addison-Wesley",
        "language": "English",
        "page_count": 352
    },
    {
        "id": 2,
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin",
        "publisher_date": "2008-08-01",
        "publisher": "Prentice Hall",
        "language": "English",
        "page_count": 464
    },
    {
        "id": 3,
        "title": "You Don’t Know JS Yet: Scope & Closures",
        "author": "Kyle Simpson",
        "publisher_date": "2020-01-28",
        "publisher": "Independently published",
        "language": "English",
        "page_count": 143
    },
    {
        "id": 4,
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher_date": "1994-10-21",
        "publisher": "Addison-Wesley",
        "language": "English",
        "page_count": 395
    },
    {
        "id": 5,
        "title": "JavaScript: The Good Parts",
        "author": "Douglas Crockford",
        "publisher_date": "2008-05-15",
        "publisher": "O’Reilly Media",
        "language": "English",
        "page_count": 176
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publisher_date: str
    language: str
    page_count: int

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    language: str
    page_count: int

@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED) 
async def create_a_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if(book['id'] == book_id):
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details= "Book Not found")
        

@app.patch("/book/{book_id}")
async def update_a_books(book_id: int, update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book['title'] = update_data.title
            book["author"]= update_data.author
            book["publisher"] = update_data.publisher
            book['language'] = update_data.language
            book['page_count'] = update_data.page_count

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_books(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Book Not found")









