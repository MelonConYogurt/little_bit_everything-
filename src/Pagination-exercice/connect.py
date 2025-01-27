import psycopg2
from faker import Faker
from config import load_config

faker = Faker()
class Book:
    def __init__(self, name: str = None, age: int = None, author: str = None, isbn: str = None):
        self.name = name or faker.word()
        self.age = age or faker.random_int(min=1, max=100)
        self.author = author or faker.name()
        self.isbn = isbn or faker.isbn10()
    
    
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def insert(data: Book, conection)-> object:
    try:
        if conection:
            with conection.cursor() as cur:
                sql_query = """ INSERT INTO public.books (name, author, age, isbn)
                    VALUES (%s,%s,%s,%s)"""
                cur.execute(sql_query, (data.name, data.author ,data.age, data.isbn ))
                conection.commit()
                print(f"Name: {data.name}, Age: {data.age}, Author: {data.author}, ISBN: {data.isbn}")
                return data
    except Exception as e:
        print(e)

if __name__ == '__main__':
    config = load_config()
    conection = connect(config)
    
    if conection:
       
        for _ in range(100):
            data = Book()
            insert(data=data, conection= conection)