# -------------------------------------------------------------
# Question:
# Write a Python program to take a multi-word string from the user.
# Then perform the following operations:
#
# (a) Count the occurrences of a given word in the string.
#
# Example:
# Enter string : orange is orange in colour
# Enter word   : orange
# Output : Count of the word is : 2
#
# (b) Form a string where the first character and the last
#     character have been exchanged.
#
# Example:
# Enter string : hello world
# Modified string : dello worlh
# -------------------------------------------------------------

# Read a string from the user
text = input("Enter a multi-word string: ")

# ---------------- Part (a) ----------------

# Read the word to search
word = input("Enter the word to count: ")

# Split the string into words
words = text.split()

# Count occurrences
count = words.count(word)

print("Count of the word is:", count)

# ---------------- Part (b) ----------------

# Check whether string has at least two characters
if len(text) >= 2:

    # Exchange first and last characters
    modified = text[-1] + text[1:-1] + text[0]

    print("Modified string:", modified)

else:
    print("String is too short to swap characters.")