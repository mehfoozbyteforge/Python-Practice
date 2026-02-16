# Q7: Frequency of elements in a list

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


# Q8: Count frequency of character in a string using dictionary

text = 'Python Programming'
dict = {}

for word in text:
    if word.isalpha():
        word = word.lower()
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1
print('\nFrequencies of Characters')
for key , value in dict.items():
    print(key,':',value)

# Q9: Merge two dictionaries manually

dict1 = {
    "math": 80,
    "science": 90
}

dict2 = {
    "science": 85,
    "english": 75
}

merged = {}

# Copy dict1 into merged
for key, value in dict1.items():
    merged[key] = value

# Merge dict2 into merged
for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("\nMerged dictionary:", merged)

# Q10: Invert a dictionary

original = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = {}

for key, value in original.items():
    inverted[value] = key

print("\nInverted dictionary:", inverted)


