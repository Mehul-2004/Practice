from operation import *

while True:

    print("____Student Management System____")

    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choose = input("Select an operation : ")

#Adding the student details

    if choose == "1":
         add_student()

#Viewing a student details
    elif choose == "2":
        view_student()

#Updating  the student details
    elif choose == "3":
         update_student()

#Deleting the student details
    elif choose == "4":
        delete_student()
#Search the student details
    elif choose == "5":
        search_student()

#Exiting the program
    elif choose == "6":
        print("Closing / Exiting the system .")
        break
    
    else :
        print("Select an appropriate operation")