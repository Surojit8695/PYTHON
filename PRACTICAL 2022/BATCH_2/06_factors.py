# -------------------------------------------------------------
# Question 6
# Write functions in Python:
# (a) number_of_factors(val): returns the number of factors.
# (b) list_of_factors(val): returns the list of factors.
# Check if the input is positive and report if not.
# -------------------------------------------------------------

# Function to return list of factors
def list_of_factors(val):

    if val <= 0:
        print("Please enter a positive number.")
        return []

    factors = []

    for i in range(1, val + 1):
        if val % i == 0:
            factors.append(i)

    return factors


# Function to return number of factors
def number_of_factors(val):

    return len(list_of_factors(val))


# Driver Program
num = int(input("Enter a positive integer: "))

if num > 0:

    print("Factors:", list_of_factors(num))
    print("Number of Factors:", number_of_factors(num))