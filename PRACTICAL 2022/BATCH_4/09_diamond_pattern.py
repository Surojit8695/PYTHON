# -------------------------------------------------------------
# Question 5(a)
# Write a Python program to print a diamond pattern.
# -------------------------------------------------------------

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):

    print(" " * (n - i - 1), end="")

    print("* " * (i + 1))

# Lower half
for i in range(n - 2, -1, -1):

    print(" " * (n - i - 1), end="")

    print("* " * (i + 1))