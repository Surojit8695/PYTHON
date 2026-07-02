# 1. Write a Program in Python to accept a list of numbers as input
# from the user and display the number of occurrences of each unique
# element using a dictionary.
# The output should clearly show each element and its frequency.
# Perform necessary Exception Handling for cases where the user
# enters a non-numeric value.

try:
    # Accept numbers from the user
    numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

    # Create an empty dictionary
    frequency = {}

    # Count the frequency of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Display the frequency of each element
    print("\nElement : Frequency")
    for key in frequency:
        print(key, ":", frequency[key])

except ValueError:
    print("Error: Please enter only numeric values.")