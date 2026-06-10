while True:

    user = input("\n Do you want to play again ?  ")

    if user.lower() == "n":
        print("Exiting the program. Goodbye!")
        break


    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    num3 = int(input("Enter third number : "))

    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest number.")
        
    elif num2>= num1 and num2 >= num3 :
        print(f"{num2} is larhest number.")
    elif num3 >= num1 and num3 >= num2:
        print(f"{num3} is largest number.")
    else :
        print("All numbers are equal.")
