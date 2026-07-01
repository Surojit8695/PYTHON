# -------------------------------------------------------------
# Question 9(a)
# Write a Python program to reverse the order of words
# in a given string.
# Example:
# Input : my name is lucky
# Output: lucky is name my
# -------------------------------------------------------------

text = input("Enter a sentence: ")

words = text.split()

words.reverse()

result = " ".join(words)

print("Reversed Sentence:")
print(result)