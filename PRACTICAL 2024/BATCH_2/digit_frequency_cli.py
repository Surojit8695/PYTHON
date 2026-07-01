# Program 2
# Write a Python program to read a multi-digit number as
# command line input and print the frequency of each digit.
#RUN IN COMMAND LINE
import sys

def frequency(num):
    d = {}

    for i in range(10):
        d[i] = num.count(str(i))

    print(d)

# Command line input
number = sys.argv[1]

frequency(number)