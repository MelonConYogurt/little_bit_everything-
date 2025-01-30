from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from model  import Book, Books, Count, Filter
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

@app.get("/books/filter/", response_model= Books )
async def get_book_data_filter(limit: int, offset: int, name: bool = False, age: bool= False, author: bool= False, isbn: bool= False):
    try:
        list_of_books =[]
        conection = Database()
        books_data = conection.get_filter(limit=limit, offset=offset, filter= Filter(name=name, age=age, author=author, isbn=isbn))
        if books_data:
            for book in books_data:
                list_of_books.append(Book(name=book[1], author=book[2], age=book[3], isbn=book[4]))
        return Books(data=list_of_books)        
    except Exception as e:
        print(e)
        return Books(data=[])


@app.get("/books/search", response_model= Books )
async def get_book_data_search_by_name(limit: int, offset: int, search: str):
    try:
        list_of_books =[]
        conection = Database()
        books_data = conection.get_search_by_name(limit=limit, offset=offset, search=search)
        if books_data:
            for book in books_data:
                list_of_books.append(Book(name=book[1], author=book[2], age=book[3], isbn=book[4]))
        return Books(data=list_of_books)        
    except Exception as e:
        print(e)
        return Books(data=[])
    
@app.get("/count/", response_model= Count )
async def get_count():
    try:
        conection = Database()
        count = conection.count()
        return Count(pages=count[0])
    except Exception as e:
        print(e)
        