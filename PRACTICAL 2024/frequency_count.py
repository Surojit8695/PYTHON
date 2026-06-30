import sys

def frequency(num):
    d = {}

    for i in range(10):
        d[i] = num.count(str(i))

    print(d)

# Command line input
number = sys.argv[1]

frequency(number)