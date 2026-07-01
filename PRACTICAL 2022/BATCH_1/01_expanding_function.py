# -------------------------------------------------------------
# Question 1
# Write a Python function expanding(numlist) that takes a list
# of integers and returns True if the absolute difference
# between each adjacent pair strictly decreases, otherwise False.
# Write a driver program to test the function.
# -------------------------------------------------------------

# Function to check the condition
def expanding(numlist):

    # List must contain at least 3 elements
    if len(numlist) < 3:
        return False

    # Calculate first absolute difference
    previous_difference = abs(numlist[1] - numlist[0])

    # Compare remaining differences
    for i in range(2, len(numlist)):

        current_difference = abs(numlist[i] - numlist[i - 1])

        # Difference must strictly decrease
        if current_difference >= previous_difference:
            return False

        previous_difference = current_difference

    return True


# Driver Program

numbers = list(map(int, input("Enter list elements separated by space: ").split()))

print(expanding(numbers))