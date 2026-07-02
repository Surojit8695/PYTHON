# 5. Write a Program in Python to accept a Sentence as input
# and create two separate Lists:
# (a) One containing words of even length
# (b) One containing words of odd length
# Display both lists with appropriate messages.

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create empty lists
even_words = []
odd_words = []

# Check the length of each word
for word in words:
    if len(word) % 2 == 0:
        even_words.append(word)
    else:
        odd_words.append(word)

# Display the results
print("\nWords with Even Length:")
print(even_words)

print("\nWords with Odd Length:")
print(odd_words)