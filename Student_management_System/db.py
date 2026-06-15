import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "M123",
    database = "stud_db"
)

cursor = conn.cursor()

query = """
create table if not exists students(
    id int AUTO_INCREMENT Primary key,
    name varchar(99),
    age int,
    gender varchar(20),
    email varchar(50),
    phone int,
    course varchar(50),
    marks int
    )"""

print("Database is connected Successfully")