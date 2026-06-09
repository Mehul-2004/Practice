import random

guess_number = random.randint(1,10)

while True:
    user_guess = int(input("Guess a number between 1 to 10 : "))

    if user_guess == guess_number:
        print("Congratulations you guessed the number correctly!")
        break

    elif user_guess < guess_number:
        print("Too low , try again!")
    else :
        print("Too high , try again!")