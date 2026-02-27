# Q1: Basic class and object

class Student:
    def greet(self):
        print("Hello, I am a student.\n")

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
s1 = Student("Mehfooz", 18)
s2 = Student("Ray\n", 22)

s1.display()
s2.display()


# Q3: Class variable vs Instance variable

class Student:
    school_name = "ABC School"   # Class variable (common)

    def __init__(self, name):
        self.name = name         # Instance variable (unique)

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school_name)


s1 = Student("Mehfooz")
s2 = Student("Ray")

s1.display()
print("------")
s2.display()


