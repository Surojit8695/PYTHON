# -------------------------------------------------------------
# Question:
# Write a Python program to create a list (taking values from the
# user) and count the occurrence of each element. Then create a
# dictionary to show the count of each element.
#
# Example:
# Input:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# Output:
# {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
# -------------------------------------------------------------

# Read number of elements
n = int(input("Enter the number of elements: "))

# Create an empty list
sample_list = []

# Read list elements from the user
print("Enter the elements:")

for i in range(n):
    element = int(input())
    sample_list.append(element)

# Create an empty dictionary
count_dict = {}

# Count the occurrence of each element
for item in sample_list:

    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Display the dictionary
print("\nOccurrence Dictionary:")
print(count_dict)