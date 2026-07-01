# -------------------------------------------------------------
# Question 3(a)
# Write a Python program to find the power of a number
# (N^P) using recursion.
# -------------------------------------------------------------

# Recursive function
def power(n, p):

    if p == 0:
        return 1

    return n * power(n, p - 1)


# Driver Program
number = int(input("Enter base: "))

exponent = int(input("Enter exponent: "))

print("Result =", power(number, exponent))