class Student:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def show(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

Name = input("Enter your name :")
Age = int(input("Enter your age : "))

student1 = Student(Name,Age)
student1.show()