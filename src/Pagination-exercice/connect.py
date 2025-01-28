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
    
    
class Database:
    def __init__(self, config: any = None):
        self.config = config or load_config()
        self.connection = self.connect()

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**self.config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def insert(self, data: Book):
        try:
            if self.connection:
                with self.connection.cursor() as cur:
                    sql_query = """ INSERT INTO public.books (name, author, age, isbn)
                        VALUES (%s,%s,%s,%s)"""
                    cur.execute(sql_query, (data.name, data.author, data.age, data.isbn))
                    self.connection.commit()
                    print(f"Name: {data.name}, Age: {data.age}, Author: {data.author}, ISBN: {data.isbn}")
                    return data
        except Exception as e:
            print(e)
            
    def get(self, limit: int = 0, offset: int = 0)-> list:
        try:
            if self.connection:
                with self.connection.cursor() as cur:
                    sql_query="""
                    SELECT * FROM public.books LIMIT %s OFFSET %s
                    """
                    cur.execute(sql_query, (limit, offset))
                    rows = cur.fetchall()
                    return rows
        except Exception as e:
            print(e)
        

if __name__ == '__main__':
    conection = Database()
    if conection:
        # for _ in range(100):
        #     data = Book()
        #     conection.insert(data=data)
        # rows = conection.get(limit= 10, offset=10)
        pass
        