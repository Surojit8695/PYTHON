# -------------------------------------------------------------
# Question 1
# Write a program in Python that reads product names and prices.
# Store them in a dictionary. After entering at least 8 products:
# (a) Search the price of a product.
# (b) Display products within a given price range.
# -------------------------------------------------------------

# Empty dictionary
products = {}

# Input at least 8 products
for i in range(8):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))

    products[name] = price

# Allow user to enter more products
while True:

    choice = input("\nDo you want to add more products? (y/n): ")

    if choice.lower() == 'n':
        break

    name = input("Enter product name: ")
    price = float(input("Enter price: "))

    products[name] = price

# Search a product
search = input("\nEnter product name to search: ")

if search in products:
    print("Price =", products[search])
else:
    print("Product not found.")

# Display products in a price range
low = float(input("\nEnter minimum price: "))
high = float(input("Enter maximum price: "))

print("\nProducts within the given price range:")

for item in products:

    if low <= products[item] <= high:
        print(item, ":", products[item])