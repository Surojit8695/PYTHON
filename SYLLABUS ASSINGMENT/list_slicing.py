# 24. Make a list of the first eight letters of the alphabet, then using the slice operation do the
# following operations:
# a. Print the first three letters of the alphabet.
# b. Print any three letters from the middle.
# c. Print the letters from any particular index to the end of the list

# Make a list of the first eight letters of the alphabet
l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# a. Print the first three letters
print("a.", l1[:3])

# b. Print any three letters from the middle
print("b.", l1[2:5])

# c. Print the letters from index 2 to the end
print("c.", l1[2:])