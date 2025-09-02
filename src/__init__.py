from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def like_span(app: FastAPI):
    print(f"server is stating...")
    await init_db()
    yield
    print(f"server has been stopped")

version = "v1"

app = FastAPI(
    version=version,
    lifespan=like_span,
    title="MY API PROJECT",
    description= "This is my API Project"
)

app.include_router(book_router, prefix =f"/api/{version}/books", tags=['Books'])




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
