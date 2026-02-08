# Q7: Reverse a list without using built-in methods

nums = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])

print("Reversed list:", reversed_list)


# Q8: Remove duplicates from a list (order maintained)

nums = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)


# Q9: Find second largest element in a list

nums = [45, 12, 89, 34, 7, 56]

largest = nums[0]
second_largest = None

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

print("Second largest element:", second_largest)


# Q10: Frequency of elements in a list

nums = [10, 20, 10, 30, 20, 10, 40]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Element frequencies:")
for key, value in freq.items():
    print(key, ":", value)
