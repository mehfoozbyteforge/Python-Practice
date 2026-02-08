# Q6: Find Factorial using for loop.
from random import randint
n = int(input('Enter a number to find factorial : '))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print('Factorial is:',fact)


# Q7: check Armstrong number.
num = int(input('Enter a number to check: '))
if num<=0:
    print('Unable to check the number whether is Armstrong or not!')
else:
    original = num
    count = 0
    temp = num
    for i in range(num):
        if temp>0:
            count += 1
            temp = temp//10
        else:
            break
    sum = 0
    temp2 = num
    for i in range(num):
        if temp2>0:
            digit = temp2%10
            sum = sum + digit**count
            temp2 = temp2//10
        else:
            break

if original==sum:
    print('The Number is Armstrong number:',sum)
else:
    print('The number is not Armstrong.')


# Q8: Find the Largest digit in the number.
give = int(input('Enter a number : '))
if give == 0:
    print('You enter \'0\'')
elif give <= -1:
    pass
else:
    high = 0
    for i in range(give):
        if give>0:
            digit = give % 10
            if digit > high:
                high = digit
            give = give // 10
        else:
            break
    print(f'The highest number is:',{high})


# Q9: Print Fibonacci Series(n terms)
rng = int(input('Enter the range for the series: '))
a = 0 
b = 1
for i in range(rng):
    print(a)
    a,b = b , a+b


# Q10: Star pattern
s = int(input('Enter a number : '))
for i in range(1,s+1):
    print('*'*i)
