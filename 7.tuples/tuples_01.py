# Q1: Create a tuple and access elements

nums = (10, 20, 30, 40, 50)

# First element
print("First element:", nums[0])

# Last element
print("Last element:", nums[-1])

# Middle elements
print("Middle slice:", nums[1:-1])


# Q2: Traverse a tuple

nums = (5, 10, 15, 20, 25)

for num in nums:
    print(num)


# Q3: Count occurrences of an element in a tuple

nums = (10, 20, 10, 30, 40, 10, 50)

search = int(input("Enter number to count: "))

count = 0

for num in nums:
    if num == search:
        count += 1

print("\nOccurrences:", count)


# Q4: Find max and min in a tuple

nums = (45, 12, 89, 34, 7, 56)

max_val = nums[0]
min_val = nums[0]

for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("\nMaximum:", max_val)
print("Minimum:", min_val)


# Q5: Convert list ↔ tuple

# List to tuple
my_list = [10, 20, 30, 40]
converted_tuple = tuple(my_list)

print("\nTuple:", converted_tuple)

# Tuple to list
my_tuple = (50, 60, 70, 80)
converted_list = list(my_tuple)

print("List:", converted_list)
