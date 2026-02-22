# Q1: Define and call a function

def greet():
    print("Hello, welcome to backend journey!")

greet()


# Q2: Function with parameters

def greet(name):
    print("Hello,", name, "welcome!")

greet("Mehfooz")
greet("Ray")


# Q3: Function with return value

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum is:", result)


# Q4: Default arguments

def greet(name="Guest"):
    print("Hello,", name)

greet("Mehfooz")   # argument diya
greet()            # argument nahi diya


# Q5: Keyword arguments

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=18, name="Mehfooz", course="BCA")