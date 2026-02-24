# Q1: Read from a file

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# Q2: Write to a file

file = open("sample.txt", "w")

file.write("Hello Mehfooz!\n")
file.write("This is file handling practice.\n")

file.close()

print("Data written successfully.")


# Q3: Append to a file

file = open("sample.txt", "a")

file.write("Appending new line...\n")
file.write("Backend journey continues.\n")

file.close()

print("Data appended successfully.")


# Q4: Count words in a file

file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()
word_count = len(words)

print("Total words:", word_count)


# Q5: Copy content from one file to another
with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.\n")


# Q6: Using with statement

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("File automatically closed.")