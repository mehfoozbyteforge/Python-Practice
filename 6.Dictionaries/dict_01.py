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
student["age"] = 22

# Delete a key-value pair
del student["course"]

print("Updated dictionary:", student)
