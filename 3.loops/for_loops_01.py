# Q1: Count Digits of a Number (without converting to string)
number = int(input('Enter a number to count it\'s digits : '))
if number == 0:
    print('Digits = 1')
else:
    count = 0
    
    for i in range(number):
        if number>0:
            count += 1
            number = number // 10
        else:
            break
    print('Digits =', count)


# Q2: Reverse a Number
inp = int(input('Enter a number : '))
reverse = 0 
for i in range(inp):
    if inp >0:
        digit = inp % 10 
        reverse = reverse*10 + digit
        inp = inp // 10
    else:
        break
print('Reversed number is :',reverse)


# Q3: Sum of digits
dig = int(input('Enter a number to get sum : '))
sum = 0
for i in range(dig):
    if dig>0:
        new = dig%10
        sum = sum + new
        dig = dig//10
    else:
        break
print('Sum of the number is :',sum)


# Q4: Prime Number check(without converting to string)
prm = int(input('Enter a number: '))
if prm<=1:
    print('The number is not prime.')
else:
    is_prime = True
    for i in range(2,int(prm**0.5+1)):
        if prm%i == 0:
            is_prime = False
            break
if is_prime:
    print('The chosen number of yours is a Prime number!')
else:
    print('The chosen number of yours is not a Prime number!')


# Q5: Count Prime number in a range.
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

count = 0

for num in range(start, end + 1):

    if num <= 1:
        continue   

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1  

print("Total prime numbers:", count)
