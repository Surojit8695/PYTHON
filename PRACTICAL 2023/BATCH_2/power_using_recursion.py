# -------------------------------------------------------------
# Question:
# Write a Python program to find the power of a number
# using recursion.
#
# Example:
# Base = 2
# Exponent = 5
# Result = 32
# -------------------------------------------------------------

# Recursive function
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

# User input
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

# Display result
print("Result =", power(base, exponent))