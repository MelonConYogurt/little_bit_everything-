from pydantic import BaseModel

class Book(BaseModel):
    name: str
    age: int
    author: str
    isbn: str
    
class Filter(BaseModel):
    name: bool | None
    age: bool | None
    author: bool | None
    isbn: bool | None
    
class Count(BaseModel):
    pages: int

class Books(BaseModel):
    data: list[Book]
    
    
    