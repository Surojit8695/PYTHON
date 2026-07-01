# -------------------------------------------------------------
# Question 4
# Write a Python program to accept two filenames as command
# line arguments. Copy contents of one file into another
# by adding line number at the beginning and line length
# at the end of each line.
# -------------------------------------------------------------

import sys

# Check command line arguments
if len(sys.argv) != 3:
    print("Usage: python 04_copy_file_with_line_number.py source.txt destination.txt")
    exit()

source = sys.argv[1]
destination = sys.argv[2]

try:

    infile = open(source, "r")
    outfile = open(destination, "w")

    line_number = 1

    for line in infile:

        text = line.rstrip()

        length = len(text)

        outfile.write(f"{line_number}. {text} ({length})\n")

        line_number += 1

    infile.close()
    outfile.close()

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")