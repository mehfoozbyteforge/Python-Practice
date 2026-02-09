# Q7: Find the longest word in a sentence

sentence = "Python programming makes backend development powerful"

words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)


# Q8: Frequency of characters in a string

text = "Programming"

freq = {}

for ch in text:
    if ch.isalpha():
        ch = ch.lower()
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print("Character frequencies:")
for key, value in freq.items():
    print(key, ":", value)


# Q9: Remove duplicate characters (order maintained)

text = "Programming"

result = ""
seen = set()

for ch in text:
    ch_low = ch.lower()
    if ch_low.isalpha() and ch_low not in seen:
        result += ch
        seen.add(ch_low)

print("Without duplicates:", result)


# Q10: Check anagram strings

s1 = "Listen"
s2 = "Silent"

# clean both strings: lowercase + letters only
clean1 = ""
clean2 = ""

for ch in s1:
    if ch.isalpha():
        clean1 += ch.lower()

for ch in s2:
    if ch.isalpha():
        clean2 += ch.lower()

# length check (quick reject)
if len(clean1) != len(clean2):
    print("Not anagrams")
else:
    freq = {}

    # count chars of first string
    for ch in clean1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # reduce counts using second string
    is_anagram = True
    for ch in clean2:
        if ch not in freq or freq[ch] == 0:
            is_anagram = False
            break
        freq[ch] -= 1

    if is_anagram:
        print("Anagrams")
    else:
        print("Not anagrams")
