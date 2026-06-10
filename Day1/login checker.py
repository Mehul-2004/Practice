username = "Admin"
password = "Password123"

user = input("Enter your username :    ")
pwd = input("Enter your password :    ")

if username == user and password == pwd:
    print("Login successful. Welcome, Admin!")
else:
    print("Login failed. Invalid username or password.")
