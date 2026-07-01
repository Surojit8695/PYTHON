# -------------------------------------------------------------
# Question:
# Write a Python program to accept two file names as command
# line arguments. Copy contents of source file into destination
# file and append the number of vowels at the end of each line.
# Report if source file is blank or not found.
# -------------------------------------------------------------

import sys

if len(sys.argv) != 3:
    print("Usage: python copy_file_with_vowel_count.py source.txt destination.txt")
    exit()

source = sys.argv[1]
destination = sys.argv[2]

try:

    with open(source, "r") as f:

        lines = f.readlines()

    if len(lines) == 0:
        print("Source file is blank.")

    else:

        with open(destination, "w") as out:

            for line in lines:

                count = 0

                for ch in line.lower():
                    if ch in "aeiou":
                        count += 1

                out.write(line.rstrip() + " Vowels=" + str(count) + "\n")

        print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")