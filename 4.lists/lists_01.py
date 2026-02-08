# Q1: List creation, indexing and slicing

nums = [10, 20, 30, 40, 50, 60]

# First element
print("First element:", nums[0])

# Last element
print("Last element:", nums[-1])

# Middle elements (excluding first and last)
print("Middle elements:", nums[1:-1])


# Q2: List operations

nums = [10, 20, 30, 40]

# append: add at the end
nums.append(50)
print("After append:", nums)

# insert: add at specific index
nums.insert(2, 25)   # index 2 par 25
print("After insert:", nums)

# remove: remove by value
nums.remove(30)
print("After remove:", nums)

# pop: remove last element
nums.pop()
print("After pop:", nums)


# Q3: Traverse a list using loop

nums = [5, 10, 15, 20, 25]
for num in nums:
    print(num)


# Q4: Sum of elements in a list

nums = [10, 20, 30, 40, 50]

total = 0
for num in nums:
    total = total + num

print("Sum of elements:", total)



# Q5: Find maximum and minimum in a list

nums = [45, 12, 89, 34, 7, 56]

max_val = nums[0]
min_val = nums[0]

for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum element:", max_val)
print("Minimum element:", min_val)


# Q6: Count even and odd numbers in a list

nums = [10, 21, 34, 45, 50, 63, 72]

even_count = 0
odd_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
