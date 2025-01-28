from pydantic import BaseModel

class Book(BaseModel):
    name: str
    age: int
    author: str
    isbn: str

class Books(Book):
    data: list[Book]
    
    
    