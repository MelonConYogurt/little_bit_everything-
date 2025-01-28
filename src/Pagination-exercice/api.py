from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from model  import Book, Books
from connect import Database

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

url = "http://127.0.0.1:8000/docs"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema= False )
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/books/", response_model= Books )
async def get_book_data(limit: int, offset: int):
    try:
        list_of_books =[]
        conection = Database()
        books_data = conection.get(limit=limit, offset=offset)
        if books_data:
            for book in books_data:
                list_of_books.append(Book(name=book[1], author=book[2], age=book[3], isbn=book[4]))
            return Books(data=list_of_books)        
    except Exception as e:
        print(e)
        return Books(data=[])