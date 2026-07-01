# -------------------------------------------------------------
# Question 7(b)
# Write a Python program to input names in any case.
# Convert uppercase letters to lowercase and lowercase
# letters to uppercase.
# -------------------------------------------------------------

name = input("Enter a name: ")

result = ""

for ch in name:

    if ch.isupper():
        result += ch.lower()

    elif ch.islower():
        result += ch.upper()

    else:
        result += ch

print("Converted Name:", result)