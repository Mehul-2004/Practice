class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        
        print(f"Name :{self.name}")
        print(f"Marks :{self.marks}")

students = []       

while True :

    print("\n 1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Select your option : ")

    if choice == "1":

        name = input("ENter your name :")
        marks = int(input("Enter your marks :"))

        student = Student(name, marks)
        students.append(student)

        print("Student added successfully.")

    elif choice == "2":

        for student in students:
            student.display()

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")