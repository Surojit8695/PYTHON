# -------------------------------------------------------------
# Question 10(a)
# A binary file "Book.dat" has the structure:
# BookNo, Book_Name, Author, Price
#
# Write a user-defined function createFile() to input
# book records and store them in Book.dat.
# -------------------------------------------------------------

import pickle

# Function to create binary file
def createFile():

    file = open("Book.dat", "wb")

    n = int(input("Enter number of books: "))

    for i in range(n):

        print("\nBook", i + 1)

        book = {}

        book["BookNo"] = int(input("Enter Book Number: "))
        book["Book_Name"] = input("Enter Book Name: ")
        book["Author"] = input("Enter Author Name: ")
        book["Price"] = float(input("Enter Price: "))

        pickle.dump(book, file)

    file.close()

    print("Book.dat created successfully.")


# Driver Program
createFile()