def get_non_empty_string(message):
    while True:
        value = input(message).strip()

        if value:
            return value
        print("Input cannot be empty.")

def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0 :
                return value
            print("Enter a positive number.")
        
        except ValueError:
            print("Please enter a valid integer.")

def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value >= 0:
                return value
            print("salary cannot be negative")
        
        except ValueError:
            print("Please enter a valid number")

def get_valid_email(message):
    while True:
      
        value = input(message).strip()
        if "@" in value and "." in value:
            return value 
        
        print("Invalid email address")

def get_valid_phone(message):
    while True:
        phone = input(message).strip()

        if phone.isdigit() and len(phone) == 10:
            return phone
        
        print("Phone number must contain exactly 10 digits")
