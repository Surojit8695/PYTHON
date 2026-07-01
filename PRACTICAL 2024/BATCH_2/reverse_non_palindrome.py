# Program 6
# Write a Python program to:
# (a) Take a list of strings as input.
# (b) Reverse only those strings which are not palindromes.

def reverse_string(word):
    return word[::-1]

n = int(input("Enter number of strings: "))

listStr = []

for i in range(n):
    listStr.append(input("Enter string: "))

print("\nResult:")

for word in listStr:

    if word == word[::-1]:
        print(word)

    else:
        print(reverse_string(word))