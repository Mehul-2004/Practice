import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "M123",
            database = "employee_management"

        )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as error:
        print("Error while connection to MySQL", error)
        return None