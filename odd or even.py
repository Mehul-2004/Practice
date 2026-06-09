print("Odd or Even Checker")

while True:

    user = input("\n Type 'exit' to quit or press Enter to continue : ")

    if user.lower() == "exit":
        print("Exiting the game . Goodbye ")
        break 

    num1 = int(input("Enter a number : "))

    if num1 % 2 == 0:
        print(f" {num1} is an even number.")
    else :
        print(f"{num1} is a odd number.")