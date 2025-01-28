from pydantic import BaseModel

class Book(BaseModel):
    name: str
    age: int
    author: str
    isbn: str

class Books(BaseModel):
    data: list[Book]
    
    
    