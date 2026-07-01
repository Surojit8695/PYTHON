# Program to print the frequency of each digit

def frequency(num):
    d = {}

    for i in range(10):
        d[i] = num.count(str(i))

    print(d)

# User input
number = input("Enter a multi-digit number: ")

frequency(number)


# string.count(value)
# The count() function is a built-in string method in Python that
#  counts how many times a specified character or substring appears in a string.
# example
# s = "banana"

# print(s.count("a"))
# output:3