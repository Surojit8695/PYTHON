# -------------------------------------------------------------
# Program: Addition of Two Numbers using Magic Method (__add__)
# -------------------------------------------------------------

class Addition:

    def __init__(self, num):
        self.num = num

    # Magic method for '+' operator
    def __add__(self, other):
        return self.num + other.num


# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Create objects
a = Addition(num1)
b = Addition(num2)

# Add two objects
print("Sum =", a + b)