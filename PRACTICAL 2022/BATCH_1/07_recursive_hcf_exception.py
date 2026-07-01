# -------------------------------------------------------------
# Question 7
# Write a recursive function to find the H.C.F. of two numbers.
# Then input a list of integers and find the H.C.F. of the
# first and fifth elements.
# Handle NameError, IndexError, ZeroDivisionError and ValueError.
# -------------------------------------------------------------

# Recursive function to find HCF
def hcf(a, b):

    if b == 0:
        return a

    return hcf(b, a % b)

try:

    # Input list elements
    numbers = list(map(int, input("Enter list elements: ").split()))

    # Find HCF of first and fifth element
    result = hcf(numbers[0], numbers[4])

    print("HCF =", result)

except IndexError:
    print("Error: List must contain at least 5 elements.")

except ValueError:
    print("Error: Enter only integers.")

except NameError:
    print("Error: Variable not defined.")

except ZeroDivisionError:
    print("Error: Division by zero.")

except Exception as e:
    print("Unexpected Error:", e)