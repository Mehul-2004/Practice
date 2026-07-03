from MODULES.employee import add_employee , view_employee


while True:

    print("\n" + "=" * 40 )
    print("Emplpoyee Management System ")
    print("=" * 40 )

    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_employee()
    
    elif choice == "2":
        view_employee()
    
    elif choice == "6":
        print("\n Thoank you for using Employee Management System ")
        break
        
    else :
        print("\n Invalid CHoice ")