# -------------------------------------------------------------
# Question 6
# Write a Python program to find:
# (a) The list of factors of a positive integer.
# (b) The number of factors.
# -------------------------------------------------------------

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive number.")

else:
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    print("Factors:", factors)
    print("Number of Factors:", len(factors))