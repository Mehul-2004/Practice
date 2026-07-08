import csv
from utils.helper import(
    get_connection,
) 
from utils.formatter import display_employee
from utils.validators import (
    get_non_empty_string,
    get_positive_integer,
    get_positive_float,
    get_valid_email,
    get_valid_phone, 
    )

search_fields = {
        "1":"employee_id",
        "2":"first_name",
        "3":"last_name",
        "4":"gender",
        "5":"age",
        "6":"department",
        "7":"designation",
        "8":"salary",
        "9":"email",
        "10":"phone",
        
    }
def get_employee_input():
    """Collect employee information from the user."""
    
    employee= {
        "first_name" : get_non_empty_string("Enter first name : ").strip(),
        "last_name" : get_non_empty_string("Enter last name : ").strip(),
        "gender" : get_non_empty_string("Enter Gender : ").strip(),
        "age" : get_positive_integer("Enter age : "),
        "department" : get_non_empty_string("Enter Department : ").strip(),
        "designation" : get_non_empty_string("Enter designation : ").strip(),
        "salary" : get_positive_float("Enter salary : "),
        "email" : get_valid_email("Enter email : ").strip(),
        "phone" : get_valid_phone("Enter phone : ").strip(),
    }
    return employee 
    #     print(employee["first_name"]),
    #     print(employee["last_name"]),
    #     print(employee["gender"]),
    #     print(employee["age"]),
    #     print(employee["department"]),
    #     print(employee["designation"]),
    #     print(employee["salary"]),
    #     print(employee["email"]),
    #     print(employee["phone"])
    # )

def add_employee():
    """Add a new employee to the database."""

    connection,cursor = get_connection()

    if connection is None:
        print("Database connection failed")
        return 

    print("\n ===========Add Employee=========")

    employee = get_employee_input()
    
    query = """
    INSERT INTO EMPLOYEE 
    (first_name,last_name,gender,age,department,designation,salary,email,phone)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values= (
        employee["first_name"],
        employee["last_name"],
        employee["gender"],
        employee["age"],
        employee["department"],
        employee["designation"],
        employee["salary"],
        employee["email"],
        employee["phone"],
        
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
    """Display all employee"""
    
    connection,cursor = get_connection()

    if connection is None:
        print("Database connection failed")
        return 
    
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
    """Search Emloyees using any supporrted field ."""
    connection,cursor = get_connection()

    if connection is None:
        print("Database connection failed")
        return 
    
    print("\n" + "=" *40)
    print("              Search Employee menu           ")
    print("=" *40)

    choice = input("Enter your choice :    ")

    try:
        if choice == "11":
            return
        if choice not in search_fields:
            print("Invalid Choice")
            return
        field = search_fields[choice]
        value = input(f"Enter {field.replace('_',' ' ).title()}: ")
        query = f"Select * from employee Where {field} = %s"
        cursor.execute(query,(value,))
        employees = cursor.fetchall()
        if employees:
            for employee in employees:
                display_employee(employee)
        else:
            print("no employee found")
    
    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()

    
def update_employee():

    connection,cursor = get_connection()

    if connection is None:
        print("Database connection failed")
        return 
    
    try:
        employee_id = input("enter your employee_id : ")

        query = "select * from employee where employee_id = %s"

        cursor.execute(query, (employee_id,))

        employee = cursor.fetchone()

        if employee:
            display_employee(employee)

            print("Update the value")
            employee = get_employee_input()
        else :
            print("No employee found")

        query = """
               update employee set
               first_name = %s,
               last_name = %s,
               gender = %s,
               age = %s,
               department = %s,
               designation = %s,
               salary = %s,
               email = %s,
               phone = %s
               where employee_id = %s
               """
        values= (
               employee["first_name"],
               employee["last_name"],
               employee["gender"],
               employee["age"],
               employee["department"],
               employee["designation"],
               employee["salary"],
               employee["email"],
               employee["phone"],
               employee_id,

                )


        cursor.execute(query,values)

        connection.commit()

        print("Updated successfully")

    except Exception as e:
        print("Error : ",e)
    
    finally :
        cursor.close()
        connection.close()

def delete_employee():

    connection,cursor = get_connection()

    if connection is None:
        print("Database connection failed")
        return 
    
    try:

        employee_id = input("Enter employee_id : ")

        query = "Select * from employee where employee_id = %s"

        cursor.execute(query , (employee_id,))

        employee = cursor.fetchone()

        if employee is None:
            print("No employee found")
            return
        
        else:
            display_employee(employee)

            confirm = input("Are you sure ? (Y/N) ")
            if confirm.upper() == "Y":
                query = "delete from employee where employee_id = %s"

                cursor.execute(query, (employee_id,))

                connection.commit()
                print("Employee Successfully deleted ")

            else :
                print("Deletion Cancelled")

    except Exception as e :
        print("Error : ",e)

    finally :
        cursor.close()
        connection.close()

def dashboard():
    """Display Employee statistics."""
    pass

    connection,cursor = get_connection()

    if connection is None:
        print("Database is not connected")
        return
    try:
        cursor.execute("Select count(*) from employee")
        total_employee = cursor.fetchone()[0]
        # print(total_employee)
        cursor.execute("Select avg(salary) from employee")
        avg_salary = cursor.fetchone()[0]
        # print(avg_salary)
        
        cursor.execute("Select max(salary) from employee")
        max_salary = cursor.fetchone()[0]
        # print(max_salary)
        cursor.execute("Select min(salary) from employee")
        min_salary = cursor.fetchone()[0]
        # print(min_salary)
        cursor.execute("Select count(Distinct department) from employee")
        department_count = cursor.fetchone()[0]
        # print(department_count)

        cursor.execute("Select department, count(*) from employee group by department")
        departments = cursor.fetchall() 
        print("\n Employees by departments")
        print("-" * 40)
        for department, count in departments:
            print(f"{department:<15} : {count}")

        
        print("\n" + "=" * 40)
        print("     Employee Dashboard")
        print("=" * 40)

        print(f"Total Employee : {total_employee}")
        print(f"Average Salary : {avg_salary:.2f}")
        print(f"Highest Salary : {max_salary:.2f}")
        print(f"Lowest Salary : {min_salary:.2f}")
        print(f"Departments : {department_count}")
        print(f"Total_departments : {departments}")

        print("=" * 40)
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        connection.close()

def export_to_csv():
    """Export all employees to a csv file."""

    connection,cursor = get_connection()

    if connection is None:
        print("Database connected failed")
        return
    try:
        query = "select * from employee"
        cursor.execute(query)
        employees = cursor.fetchall()

        if not employees:
            print("No employees found")
            return

        with open(
            "exports/employees.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow([
                "Employee ID",
                "First Name",
                "Last Name",
                "Gender",
                "Age",
                "Department",
                "Designation",
                "Salary",
                "Email",
                "Phone"
            ])
        for employee in employees:
            writer.writerow(employee)
            print("\nEmployees exported successfully.")
            print("Location: exports/employees.csv")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()