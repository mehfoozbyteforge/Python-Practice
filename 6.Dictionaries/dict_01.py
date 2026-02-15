# Q1: Create a dictionary and access values using keys

student = {
    "name": "Mehfooz",
    "age": 18,
    "course": "BCA",
    "city": "Kolkata"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])


# Q2: Add, update and delete key-value pairs

student = {
    "name": "Mehfooz",
    "age": 21,
    "course": "BCA"
}

# Add a new key-value pair
student["city"] = "Kolkata"

# Update an existing value
student["age"] = 18

# Delete a key-value pair
del student["course"]

print("\nUpdated dictionary:", student)


# Q3: Trasverse a Dictionary using loops.

student = {
    "name": "Mehfooz",
    "age": 21,
    "course": "BCA"
}
print('\nKeys:')
for key in student.keys():
    print(key) 

print('\nvalues:')
for value in student.values():
    print(value)

print('\nKey-Value pairs:')
for key , value in student.items():
    print('keys:',key,',','Value:',value)


# Q4: Sum of all values in a dictionary

marks = {
    "math": 85,
    "science": 90,
    "english": 78,
    "history": 88
}

total = 0

for value in marks.values():
    total += value

print("\nTotal marks:", total)



# Q5: Find key with maximum value

marks = {
    "math": 85,
    "science": 92,
    "english": 78,
    "history": 88
}

max_key = None
max_value = None

for key, value in marks.items():
    if max_value is None or value > max_value:
        max_value = value
        max_key = key

print("Highest marks subject:", max_key)
print("Marks:", max_value)


# Q6: Check if key exists

student = {
    "name": "Mehfooz",
    "age": 22,
    "city": "Kolkata"
}

search_key = input("Enter key to search: ")

if search_key in student:
    print("Key exists. Value:", student[search_key])
else:
    print("Key does not exist.")
