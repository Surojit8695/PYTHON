sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Sort words in decreasing order of length
words.sort(key=len,reverse=True)

print("Words in decreasing order of length:")

for word in words:
    print(word, "->", len(word))