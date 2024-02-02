from fastapi import FastAPI
import pymysql.cursors
from pymysql import Error

app = FastAPI()

DB_USER = "root"
DB_PASSWORD = "admin"
DB_HOST = "db"
DB_PORT = "3306"
DATABASE = "mysql_db"

def __create_connection():
    connection = None
    try:
        connection = pymysql.connect(host=DB_HOST,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    database=DATABASE,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
    except Error as e:
        print(e)
        return None
    return connection

@app.get("/")
def read_root():
    conn = __create_connection()
    print(conn)
    return {"Hello": "World"}

