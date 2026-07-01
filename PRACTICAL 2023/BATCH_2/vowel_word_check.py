# -------------------------------------------------------------
# Question:
# Write a program in Python that checks whether any word in a
# given string starts and ends with a vowel.
# Return True if a word matches the condition;
# otherwise return False.
#
# Sample Data:
# "Red Orange White" -> True
# "Red White Black" -> False
# -------------------------------------------------------------

# Read the string
text = input("Enter a string: ")

# List of vowels
vowels = "aeiouAEIOU"

# Split the string into words
words = text.split()

found = False

# Check each word
for word in words:

    if word[0] in vowels and word[-1] in vowels:
        found = True
        break

print(found)