# Q6: Find Factorial using for loop.
from random import randint
n = int(input('Enter a number to find factorial : '))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print('Factorial is:',fact)
