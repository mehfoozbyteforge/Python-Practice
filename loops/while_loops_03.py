# Q1: Count digits using while loop.
num = int(input('Enter a number : '))
if num < 0:
    print('Try number greater than \'0\'')
elif num ==0:
    print('Digit: 1')
else:
    count = 0
    while num>0:
        count +=1
        num = num // 10
    print('Digits:',count)


# Q2: Reverse number using while loop.
n = int(input('Enter a nunber : '))
if n < 0:
    print('Try using number greater than \'0\'')
elif n == 0:
    print('Unable to reverse the number.')
else:
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse*10 + digit
        n = n // 10
    print('Reversed number is:',reverse)


# Q3: Menu-driven program using while loop
while True:
    choice = input('Press any key to continue: ')

    if choice == 'q':
        print('Program exitted!')
        break
    else:
        print('Program is running....')