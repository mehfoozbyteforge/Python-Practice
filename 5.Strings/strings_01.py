# Q1: String indexing and slicing

text = "pythonprogramming"

# First character
print("First character:", text[0])

# Last character
print("Last character:", text[-1])

# Middle part (excluding first and last)
print("Middle part:", text[1:-1])

# Every second character
print("Every second character:", text[::2])



# Q2: Reverse a string without slicing

text = "python"

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)


# Q3: Vowels and consonants count.

text = 'Python Programming'

vowels = 'aeiouAEIOU'
vowels_counts = 0
consonant_count =0
for wo in text:
    if  wo.isalpha():
        if wo in vowels:
            vowels_counts += 1
        else:
            consonant_count += 1
print('vowels:',vowels_counts)
print('consonants:',consonant_count)

# Q4: Check whethe string is a Palindrome
word = input('Enter a word: ')

cleaned = ''
for wo in word:
    if wo.isalpha():
        cleaned += wo.lower()
reversed = ""
for wo in cleaned:
        reversed = wo + reversed
if cleaned == reversed:
    print('Yes it is a palindrome string!')
else:
    print('No its not a Palindrome string!')


# Q5: Count characters without Space.
wrd = input('Enter a word: ')
character_count = 0
for wr in wrd:
    if wr.isalpha():
        character_count += 1
print('No of Characters:',character_count)


# Q6: Convert string case manually

text = "PyThOn ProGraMMing"
result = ""

for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch   # space or symbol

print("Converted string:", result)

