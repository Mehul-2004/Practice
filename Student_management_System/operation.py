from db import conn , cursor


#Add students

def add_student():
    try:
        name = input("Enter student name : ")
        marks = input("Enter student marks : ")

        query = "insert into students(name,marks) values(%s,%s)"

        values = (name,marks)
        cursor.execute(query,values)
        conn.commit()

        print("Student details added successfully")
    
    except ValueError:
        print("Marks must be a number")

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


#searching student Details
def search_student():

    # while True:
        print("1. id")
        print("2. name")
        print("3. marks")

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
                      ID : {row[0]})
                      Name : {row[1]})
                      Marks : {row[2]}
                      """)
        
        else:
            print("No student found")