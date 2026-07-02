# -------------------------------------------------------------
# Question 1
# Write a program in Python that reads product names and prices.
# Store them in a dictionary.
#
# Menu Driven Program using Class:
# 1. Add Product
# 2. Search Product Price
# 3. Display Products within Price Range
# 4. Display All Products
# 5. Exit
# -------------------------------------------------------------

# Class Definition
class Product:

    # Constructor
    def __init__(self):
        self.products = {}

    # Method to add a product
    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        self.products[name] = price
        print("Product added successfully.")

    # Method to search a product
    def search_product(self):
        if len(self.products) == 0:
            print("No products available.")
            return

        name = input("Enter product name to search: ")

        if name in self.products:
            print("Price =", self.products[name])
        else:
            print("Product not found.")

    # Method to display products within a price range
    def display_range(self):
        if len(self.products) == 0:
            print("No products available.")
            return

        low = float(input("Enter minimum price: "))
        high = float(input("Enter maximum price: "))

        print("\nProducts within the given price range:")

        found = False

        for item in self.products:
            if self.products[item] >= low and self.products[item] <= high:
                print(item, ":", self.products[item])
                found = True

        if found == False:
            print("No products found in this price range.")

    # Method to display all products
    def display_all(self):
        if len(self.products) == 0:
            print("No products available.")
            return

        print("\nProduct List")

        for item in self.products:
            print(item, ":", self.products[item])


# Main Program

obj = Product()

while True:

    print("\n------ PRODUCT MENU ------")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Display Products within Price Range")
    print("4. Display All Products")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_product()

    elif choice == 2:
        obj.search_product()

    elif choice == 3:
        obj.display_range()

    elif choice == 4:
        obj.display_all()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")