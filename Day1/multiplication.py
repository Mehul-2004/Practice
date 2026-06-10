while True :
    user = input(  "\n Type 'exit' to quit or press Enter to continue : "   )

    if user.lower() == "exit" :
        print("Exiting the multiplication table. Goodbye!")
        break

    num = int(input("Enter a number : "))

    for i in range(1,11):
        print(num , "x" , i , "=" , num * i)
