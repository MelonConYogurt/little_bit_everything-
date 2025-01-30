from pydantic import BaseModel

class Book(BaseModel):
    name: str
    age: int
    author: str
    isbn: str
    
class Filter(BaseModel):
    name: bool = False
    age: bool = False
    author: bool = False
    isbn: bool = False
    
class Count(BaseModel):
    pages: int

class Books(BaseModel):
    data: list[Book]
    
    
    