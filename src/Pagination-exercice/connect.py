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
        
class Filter:
    def __init__(self, name: bool = None, age: bool = None, author: bool = None, isbn: bool = None):
        self.name = name
        self.age = age
        self.author = author
        self.isbn = isbn
    
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
                    return rows if rows else []
        except Exception as e:
            print(e)
            return []
        
    def get_filter(self, filter: Filter, limit: int = 0, offset: int = 0, search: str = None)-> list: 
        try:
            if self.connection:
                with self.connection.cursor() as cur:
                    filter_string = ""
                    list_of_filters = []
                    if filter.name is True:
                        list_of_filters.append("name ASC")
                    elif filter.name is False:
                        list_of_filters.append("name DESC")
                    if filter.age is True:
                        list_of_filters.append("age ASC")
                    elif filter.age is False:
                        list_of_filters.append("age DESC")
                    if filter.author is True:
                        list_of_filters.append("author ASC")
                    elif filter.author is False:
                        list_of_filters.append("author DESC")
                    if filter.isbn is True:
                        list_of_filters.append("isbn ASC")
                    elif filter.isbn is False:
                        list_of_filters.append("isbn DESC")
            
                    if list_of_filters:
                        filter_string = "ORDER BY " + ",".join(list_of_filters)
                        
                    sql_query=f"""
                    SELECT * FROM public.books
                    WHERE "name" LIKE %s
                    {filter_string}
                    LIMIT %s OFFSET %s 
                    """
                    cur.execute(sql_query, (f"%{search}%", limit, offset))
                    rows = cur.fetchall()
                    return rows if rows else []
        except Exception as e:
            print(e)
            return []
            
    def get_search_by_name(self, limit: int = 0, offset: int = 0, search: str = None)-> list:
        try:
            if search and self.connection:
                with self.connection.cursor() as cur:
                    sql_query = """
                    SELECT * FROM public.books WHERE "name" LIKE %s LIMIT %s OFFSET %s
                    """
                    cur.execute(sql_query, (f"%{search}%", limit, offset))
                    rows = cur.fetchall()
                    return rows if rows else []
            else:
                return []
        except Exception as e:
            print(e)
            
    def count(self)-> int:
        try:
            if self.connection:
                with self.connection.cursor() as cur:
                    sql_query="""
                    SELECT COUNT(*) AS total
                    FROM public.books;
                    """
                    cur.execute(sql_query,())
                    count = cur.fetchone()
                    return count
        except Exception as e:
            print(e)
            return []
        
if __name__ == '__main__':
    conection = Database()
    if conection:
        # for _ in range(300):
        #     data = Book()
        #     conection.insert(data=data)
        # rows = conection.get(limit= 10, offset=10)
        # count = conection.count()
        # print(count[0])
        pass