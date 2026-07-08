from db import conn , cursor


#Add students

def add_student():
    try:
        name = input("Enter student name : ")
        age = int(input("Enter your age :"))
        gender = input( "Gender (M/F) :")
        if gender.upper() not in ["MALE","FEMALE"]:
            print("Invalid Gender")
            return   
        email = input("Enter your mail id : ")
        if "@" not in email :
            print("Invalid Email")
            return
        phone = input("Enter your contact number : ")
        course = input("Which course : ")
        marks = int(input("Enter student marks : "))

        query = "insert into students(name,age,gender,email,phone,course,marks) values(%s,%s,%s,%s,%s,%s,%s)"

        values = (name,age,gender,email,phone,course,marks)
        cursor.execute(query,values)
        conn.commit()

        print("Student details added successfully")
    
    except ValueError:

        print("Please enter valid numeric values")

    except Exception as e:

        print("Error :", e)
#View Students

def view_student():

    cursor.execute("Select * from students")

    data = cursor.fetchall()

    print("__All Students__")

    for row in data:
        print(row)

#Update Student

def update_student():

    name = input("Enter student name :")
    new_marks =input("Enter the marks : ")
    query = "update students set marks = %s where name = %s"
    values = (new_marks,name)
    cursor.execute(query,values)
    if cursor.rowcount > 0:

         print("Marks updated successfully")

    else:

        print("Student not found")

    conn.commit()

    print("Marks are updated")

#Delete data

def delete_student():
    name = input("Enter the name : ")
    query = "delete from students where name = %s"
    values = (name,)
    cursor.execute(query,values)

    conn.commit()
    print("Data Deleted successfully")
    if cursor.rowcount > 0:
        print("Updated Successfully")
    else:
        print("Student not found")


#searching student Details
def search_student():

    # while True:
        print("1. id")
        print("2. name")
        print("3. age")
        print("4. gender")
        print("5. email")
        print("6. phone")
        print("7. course")
        print("8. marks")

        choose = input("What do yo want to search : ")

        if choose == "1":
            id = input("Enter student id : ")

            query = "select * from students where id = %s"

            cursor.execute(query,(id,))

        elif choose == "2":
            name = input("Enter student name : ")

            query = "select * from students where name = %s"

            cursor.execute(query,(name,))

        elif choose == "3":
            age = input("Enter student age : ")

            query = "select * from students where age = %s"

            cursor.execute(query,(age,))
       
        elif choose == "4":
            gender = input("Enter student gender : ")

            query = "select * from students where gender = %s"

            cursor.execute(query,(gender,))
        
        elif choose == "5":
            email = input("Enter student email : ")

            query = "select * from students where email = %s"

            cursor.execute(query,(email,))
        
        elif choose == "6":
            phone = input("Enter student phone : ")

            query = "select * from students where phone = %s"

            cursor.execute(query,(phone,))
        
        elif choose == "7":
            course = input("Enter student course : ")

            query = "select * from students where course = %s"

            cursor.execute(query,(course,))


        elif choose == "8":
            marks = input("Enter student marks : ")

            query = "select * from students where marks = %s"

            cursor.execute(query,(marks,))

        
        else :
            print("Invalid choice")
            return
            # break
        
        data = cursor.fetchall()

        if data:
            print("\n --- Search Results ---")
            for row in data:
               print(f"""
                    ID        : {row[0]}
                    Name      : {row[1]}
                    Marks     : {row[2]}
                    Age       : {row[3]}
                    Gender    : {row[4]}
                    Email     : {row[5]}
                    Phone No  : {row[6]}
                    Course    : {row[7]}
""")
        
        else:
            print("No student found")