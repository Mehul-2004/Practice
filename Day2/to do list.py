work = []

while True:

    print("\n 1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Enter your option : "))

    if choice == 1:
        task = input("Enter a task : ")
        work.append(task)
    
        print("Task Added ")

    elif choice == 2:

        print("\n Your Tasks.")
        for task in work:
            print("-",task)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break   

    else :
        print("Invalid option. Please try again.")
