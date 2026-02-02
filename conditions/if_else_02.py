# Q1: Divisible by 5

print('Generating number.....!')
from random import randint
number = randint(5,50)
print(f'The generated number is \'{number}\'')
if number % 5 == 0:
    print(f'The {number} is divisible by 5.')
else:
    print(f'{number} is not divisible by 5.')


# Q2: Pass or Fail
marks = randint(1,100)
print(f'The marks of the student is {marks}!')
if 90<=marks<=100:
    print(f'The STUDENT is passed by promoted with GRADE \' A\' ')
elif 80<=marks<=89:
    print(f'The STUDENT is passed and promoted with GRADE \'B\'')
elif 70<=marks<=79:
    print(f'The STUDENT is passed and promoted with GRADE \'C\'')
elif 33<=marks<=69:
    print(f'The STUDENT is passed and promoted with GRADE \'D\'')
else:
    print('The STUDENT cannot clear the exam and \'FAILED\'')


# Q3: Leap year detection
year = int(input('Enter Year to chech whether is \'LEAP YEAR\' or \'NOT\' : '))
if (year % 400 == 0) or (year % 4 == 0 and year % 100!=0):
    print(f'The year {year} was LEAP YEAR!')
else:
    print(f'The year {year} was not LEAP YEAR.')


# Q4: Greatest number between three numbers.
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
if a>b and a>c:
    print(f'{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater than {a} and {c}')
elif c>a and c>b:
    print(f'{c} is greater than {a} and {b}')
elif a==b==c:
    print('All the three number you give are same!')