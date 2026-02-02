# Q1: Number positive ya negative.

print('Generating number......!')
from random import randint 
n = randint(-10,10)
print(f'The generated number is {n}')
if n<=-1:
    print('The number is negative!')
elif n>=1:
    print('The generated number is positive!')
else:
    print('You got Zero!')


# Q2: Even or odd

print('Generating number....!')
m = randint(1,20)
print(f'The generated number is {m}')
if m % 2 == 0:
    print('The number is Even')
else:
    print('The number is odd')

# Q3: Greater number
a = int(input('Enter a : '))
b = int(input('Enter b : '))
if a>b:
    print(f'a is greater than b : winner is \' {a}\'')
elif b>a:
    print(f'b is greater than a : winner is \'{b}\'')
else:
    print('Both value are same, try again! ')

# Q4: Voting age criteria
age = int(input('Enter your age : '))
if age >=18:
    print(f'Congratulations! you are eligible for voting.')
else:
    print(f'Sadly! you are not eligible for voting you have \n to wait till 18.')