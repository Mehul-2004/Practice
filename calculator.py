print("----Smart Calculator----")

while True:
    user=input("\n Type 'exit' to quit or press Enter to continue : ")

    if user.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    num1=float(input(" Enter a number : "))
    num2=float(input(" Enter second number : "))

    print("Select the operation : ")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")

    operator = input("Select an operator : ")

    if operator == '1':
        print(f"Result : {num1} + {num2} = {num1 + num2}")
    elif operator == '2':
        print(f"Result : {num1} - {num2} = {num1 - num2}")
    elif operator == '3':
        print(f"Result : {num1} * {num2} = {num1 * num2}")
    elif operator == '4':
        if num1 != 0:
            print(f"Result : {num1} / {num2} = {num1 / num2 }")
        else:
            print("Error : Division by zero is not allowed.")
    else:
        print("Invalid operator selected.")
