# -------------------------------------------------------------
# Question 6(b)
# Write a Python program to create a lambda function
# that adds 15 to a given number.
# -------------------------------------------------------------

# Lambda Function
add15 = lambda x: x + 15

# Driver Program
number = int(input("Enter a number: "))

print("Result =", add15(number))