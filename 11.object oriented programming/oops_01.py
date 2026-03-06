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


# Q4: Class Methods vs Instance Methods

class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print("\nStudent Name:", self.name)

    # Class method
    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)


s1 = Student("Mehfooz")

# Calling instance method
s1.show_name()

# Calling class method
Student.show_school()



# Q5: Inheritance example

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):  # Inheriting from Person
    def __init__(self, name, roll):
        super().__init__(name)  # Call parent constructor
        self.roll = roll

    def show_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)


s1 = Student("Mehfooz", 101)

print('\n')
s1.greet()        # inherited method
s1.show_details() # child method



# Q6: Method Overriding

class Person:
    def greet(self):
        print("Hello, I am a person")


class Student(Person):
    def greet(self):
        print("Hello, I am a student")


p1 = Person()
s1 = Student()

print('\n')
p1.greet()
s1.greet()


# Q7: Encapsulation example

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount(1000)

acc.deposit(500)
print('\n')
acc.show_balance()