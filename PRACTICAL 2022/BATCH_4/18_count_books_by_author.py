# -------------------------------------------------------------
# Question 10(b)
# Write a function countRec(Author) that accepts an
# author's name and counts the number of books written
# by that author in Book.dat.
# -------------------------------------------------------------

import pickle

# Function to count books by author
def countRec(author_name):

    count = 0

    try:

        file = open("Book.dat", "rb")

        while True:

            book = pickle.load(file)

            if book["Author"].lower() == author_name.lower():
                count += 1

    except EOFError:
        file.close()

    return count


# Driver Program
author = input("Enter Author Name: ")

print("Number of Books =", countRec(author))