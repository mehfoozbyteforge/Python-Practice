# Q7: Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5 + 1)):
        if n%i == 0:
            return False
        
    return True
num = int(input('Enter number to check: '))
if is_prime(num):
    print('Prime Number')
else:
    print('Not a prime Number ')

# Q8: Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
num = int(input('Enter a number: '))
print(f'Factorial: {factorial(num)}')

# Q9: Fibonacci using recursion

def fibonacci(n):
    if n == 0:   # Base case 1
        return 0
    if n == 1:   # Base case 2
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter position: "))
print("Fibonacci value:", fibonacci(num))


# Q10: : Lambda function 

add = lambda a,b : a+b
result = add (10,20)
print(f'Sum:',result)

# Q11: Using *args

def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(total_sum(10, 20))
print(total_sum(5, 15, 25))
print(total_sum(1, 2, 3, 4, 5))

# Q12: Using **kwargs

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Mehfooz", age=21, course="BCA")