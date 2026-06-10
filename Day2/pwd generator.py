import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

PASSWORD = ""
for i in range(8):
    PASSWORD += random.choice(characters)

print("Password Generated",PASSWORD)
