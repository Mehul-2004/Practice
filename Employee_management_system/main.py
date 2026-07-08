from services.employee_service import (
    add_employee ,
    view_employee ,
    search_employee ,
    update_employee ,
    delete_employee,
    dashboard
    )
from utils.menu import display_main_menu
def main():
    while True:

        display_main_menu()


        choice = input("Enter your choice : ")

        if choice == "1":
            add_employee()
        
        elif choice == "2":
            view_employee()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()
        
        elif choice == "5":
            delete_employee()
        
        elif choice == "6":
            dashboard()
        
        elif choice == "7":
            print("\n Thank you for using Employee Management System ")
            break
            
        else :
            print("\n Invalid Choice ")

if __name__ == "__main__":
    main()