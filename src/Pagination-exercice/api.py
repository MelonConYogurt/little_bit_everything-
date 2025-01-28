from fastapi import FastAPI
from model  import Book, Books
from connect import Database
from config import load_config

app = FastAPI()
config = load_config()
conection = Database()

@app.get("/books/", response_model= Books )
async def root():
    return {"message": "Hello World"}