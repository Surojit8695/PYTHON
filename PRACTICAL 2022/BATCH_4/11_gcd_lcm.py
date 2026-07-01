# -------------------------------------------------------------
# Question 6(a)
# Write a Python program to calculate GCD and LCM of two numbers.
# -------------------------------------------------------------

# Function to calculate GCD
def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


# Driver Program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

g = gcd(num1, num2)

l = (num1 * num2) // g

print("GCD =", g)
print("LCM =", l)