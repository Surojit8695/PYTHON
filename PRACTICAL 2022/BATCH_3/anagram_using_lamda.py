# Program to find all anagrams of a string without lambda and filter

# Original list
words = ['beda', 'abce', 'bcda', 'cbea', 'adcb']

# Target string
target = "abcd"

# Empty list to store anagrams
result = []

# Check each word
for word in words:
    if sorted(word) == sorted(target):
        result.append(word)

print("Original List:")
print(words)

print("\nAnagrams of", target, "are:")
print(result)