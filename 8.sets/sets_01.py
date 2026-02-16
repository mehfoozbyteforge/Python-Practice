# Q1: Create and perform basic set operations

nums = {10, 20, 30, 40}

print("Original set:", nums)

# Add element
nums.add(50)
print("After adding 50:", nums)

# Remove element
nums.remove(20)
print("After removing 20:", nums)

# Membership check
if 30 in nums:
    print("30 exists in the set")
else:
    print("30 does not exist")


# Q2: Remove duplicates from list using set

nums = [10, 20, 10, 30, 40, 20, 50]

unique_nums = list(set(nums))

print("\nOriginal list:", nums)
print("After removing duplicates:", unique_nums)


# Q3: Union of two sets (manual)

set1 = {10, 20, 30}
set2 = {30, 40, 50}

union_set = set()

# Add elements of set1
for num in set1:
    union_set.add(num)

# Add elements of set2
for num in set2:
    union_set.add(num)

print("\nUnion:", union_set)


# Q4: Intersection of two sets (manual)

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersection_set = set()

for num in set1:
    if num in set2:
        intersection_set.add(num)

print("\nIntersection:", intersection_set)


# Q5: Difference of two sets (manual)

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

difference_set = set()

for num in set1:
    if num not in set2:
        difference_set.add(num)

print("\nDifference (set1 - set2):", difference_set)


# Q6: Check subset manually

set1 = {10, 20}
set2 = {10, 20, 30, 40}

is_subset = True

for num in set1:
    if num not in set2:
        is_subset = False
        break

if is_subset:
    print("set1 is a subset of set2")
else:
    print("set1 is NOT a subset of set2")
