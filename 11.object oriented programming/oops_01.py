# Q1: Basic class and object

class Student:
    def greet(self):
        print("Hello, I am a student.")

# Creating object
s1 = Student()

# Calling method
s1.greet()

# Q2: Constructor and instance variables

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
s1 = Student("Mehfooz", 21)
s2 = Student("Ray", 22)

s1.display()
s2.display()