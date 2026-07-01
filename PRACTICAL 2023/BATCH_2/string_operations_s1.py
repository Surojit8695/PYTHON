# -------------------------------------------------------------
# Question:
# Consider the string:
#
# S1 = "I Love ICE CREAM"
#
# Perform the following operations:
#
# (a) Print all words containing the letter 'e'
# (b) Output: "I love ice cream"
# (c) Reverse the string
# (d) Check whether S1 starts with 'I'
# (e) Replace "ICE CREAM" with "HOCKEY"
# -------------------------------------------------------------

S1 = "I Love ICE CREAM"

print("Original String:", S1)

# (a)
print("\nWords containing 'e':")

for word in S1.split():

    if 'e' in word.lower():
        print(word)

# (b)
print("\nLowercase String:")
print(S1.lower())

# (c)
print("\nReversed String:")
print(S1[::-1])

# (d)
print("\nStarts with 'I'?")
print(S1.startswith("I"))

# (e)
print("\nAfter Replacement:")
print(S1.replace("ICE CREAM", "HOCKEY"))