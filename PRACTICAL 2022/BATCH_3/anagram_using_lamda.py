# Program to find all anagrams of a string using lambda

# Original list
words = ['beda', 'abce', 'bcda', 'cbea', 'adcb']

# Target string
target = "abcd"

# Find anagrams using lambda and filter
result = list(filter(lambda x: sorted(x) == sorted(target), words))
# filter() keeps only those words for which the lambda function returns True.
print("Original List:")
print(words)

print("\nAnagrams of", target, "are:")
print(result)