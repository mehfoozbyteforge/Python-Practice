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