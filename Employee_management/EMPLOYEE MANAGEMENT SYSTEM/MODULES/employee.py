from DATABASE.mysql_db import connect_db

def add_employee():
    connection = connect_db()

    if connection is None:
        print("Failed to connect database ")
        return
    
    cursor = connection.cursor()

    print("\n ===========Add Employee=========")

    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")
    gender = input("Enter Gender : ")
    age = input("Enter age : ")
    department = input("Enter Department : ")
    designation = input("Enter designation : ")
    salary = float(input("Enter salary : "))
    email = input("Enter email : ")
    phone = input("Enter phone : ")
    joining_date = input("Enter joining_date : ")

    query = """
    INSERT INTO EMPLOYEE 
    (first_name,last_name,gender,age,department,designation,salary,email,phone,joining_date)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values= (
        first_name,
        last_name,
        gender,
        age,
        department,
        designation,
        salary,
        email,
        phone,
        joining_date
    )

    try:
        cursor.execute(query,values)
        connection.commit()

        print("\n Employee Added successfully")

    except Exception as e:
        print("\n Error",e)

    finally:
        cursor.close()
        connection.close()