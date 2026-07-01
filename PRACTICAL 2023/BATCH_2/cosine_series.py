# -------------------------------------------------------------
# Question:
# Write a Python program to calculate the cosine series:
#
# cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
#
# Input:
# x in degrees
# Number of terms
# -------------------------------------------------------------

import math

# Read input
x = float(input("Enter angle in degrees: "))
n = int(input("Enter number of terms: "))

# Convert degree to radian
x = math.radians(x)

result = 0

for i in range(n):

    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)

    result += term

print("cos(x) =", result)