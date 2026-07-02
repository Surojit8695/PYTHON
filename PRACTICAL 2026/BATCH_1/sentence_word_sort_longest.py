# 4. Write a Program in Python to accept a Sentence as input
# and store each word in a list.
# Display the list of words in alphabetical order.
# Also display the longest word present in the sentence,
# along with its length.

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Store each word in a list
words = sentence.split()

# Sort the list in alphabetical order
words.sort()

# Display the sorted list
print("\nWords in Alphabetical Order:")
print(words)

# Find the longest word
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Display the longest word and its length
print("\nLongest Word:", longest_word)
print("Length:", len(longest_word))