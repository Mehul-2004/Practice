while True:

    print("This is a sticky note app.")

    print("\n 1) Write Notes")
    print("2) Read Notes")
    print("3) Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        note=input("Write your notes here :")
        with open("notes.txt","w") as file:
            file.write(note + "\n")

        print("Notes Saved")

    elif choice == 2:

        try:
            with open("notes.txt","r") as file:
                print("\n Your Notes : ")
                print(file.read())
        except FileNotFoundError:
            print("No notes found. Please write some notes first.")
        
    elif choice == 3:
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

            