# -------------------------------------------------------------
# Question 4(b)
# Write a Python function to find the length of a string.
# -------------------------------------------------------------

# Function to calculate string length
def string_length(text):

    count = 0

    for ch in text:
        count += 1

    return count


# Driver Program
text = input("Enter a string: ")

print("Length =", string_length(text))