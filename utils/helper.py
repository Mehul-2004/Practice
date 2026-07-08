from database.mysql_db import connect_db

def get_connection():
    connection = connect_db()
    if connection is None:
        return None, None
    
    return connection, connection.cursor()

