from DATABASE.mysql_db import connect_db

def display_employee(employee):
            print(f"Employee ID : {employee[0]}")
            print(f"Name        : {employee[1]} {employee[2]}")
            print(f"Gender      : {employee[3]}")
            print(f"Age         : {employee[4]}")
            print(f"Department  : {employee[5]}")
            print(f"Designation : {employee[6]}")
            print(f"Salary      : {employee[7]}")
            print(f"Email       : {employee[8]}")
            print(f"Phone       : {employee[9]}")
            print(f"Joining Date: {employee[10]}")
            print("-" * 40)

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


def view_employee():
    connection = connect_db()

    if connection is None:
        print("Failed to connect database")
        return
    
    cursor = connection.cursor()

    query = "Select * from employee"

    try:
        cursor.execute(query)

        employees = cursor.fetchall()

        if not employees :
            print("\n No employees found")
            return
        
        print("\n=============Employee list=================\n")

        for employee in employees:
            display_employee(employee)

    except Exception as e:
        print("\n Error",e)

    finally :
        cursor.close()
        connection.close()

def search_employee():
     connection = connect_db()

     if connection is None:
          print("Database is not connected")
          return
     
     cursor = connection.cursor()

     print("\n" + "=" *40)
     print("              Search Employee menu           ")
     print("=" *40)

     print("1. Search by Employee ID")
     print("2. Search by First Name")
     print("3. Search by Last Name")
     print("4. Search by Gender")
     print("5. Search by Age")
     print("6. Search by Department")
     print("7. Search by Designation")
     print("8. Search by Salary")
     print("9. Search by Email")
     print("10. Search by Phone")
     print("11. Exit")

     choice = input("Enter your choice :    ")

     try:
          if choice == "1":
            employee_id = input("Enter Employee_ID : ")
            query = "Select * from employee where employee_id = %s"
            cursor.execute(query,(employee_id,))
            employee = cursor.fetchone()
            if employee:
                display_employee(employee)
            else:
                print("no employee found")

          elif choice == "2":
            first_name = input("Enter first_name : ")
            query = "Select * from employee where first_name = %s"
            cursor.execute(query,(first_name,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")
          
          elif choice == "3":
            last_name = input("Enter last_name : ")
            query = "Select * from employee where last_name = %s"
            cursor.execute(query,(last_name,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")
          
          elif choice == "4":
            gender = input("Enter gender : ")
            query = "Select * from employee where gender = %s"
            cursor.execute(query,(gender,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "5":
            age = input("Enter age : ")
            query = "Select * from employee where age = %s"
            cursor.execute(query,(age,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "6":
            department = input("Enter department : ")
            query = "Select * from employee where department = %s"
            cursor.execute(query,(department,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "7":
            designation = input("Enter designation : ")
            query = "Select * from employee where designation = %s"
            cursor.execute(query,(designation,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "8":
            salary = input("Enter salary : ")
            query = "Select * from employee where salary = %s"
            cursor.execute(query,(salary,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "9":
            email = input("Enter email  : ")
            query = "Select * from employee where email  = %s"
            cursor.execute(query,(email ,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")

          elif choice == "10":
            phone = input("Enter phone : ")
            query = "Select * from employee where phone = %s"
            cursor.execute(query,(phone,))
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
            else:
                print("no employee found")
            
          elif choice == "11":

            return

          else:

            print("Invalid choice.")

     except Exception as e:

        print("Error:", e)

     finally:

        cursor.close()
        connection.close()