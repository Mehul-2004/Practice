import mysql.connector
from config import DB_CONFIG


def connect_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None