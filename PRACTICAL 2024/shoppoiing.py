class ShoppingCart:

    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    def display(self):
        if len(self.cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("Items in Shopping Cart:")
            for i in self.cart:
                print(i)


obj = ShoppingCart()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Display Cart")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = input("Enter item: ")
        obj.add_item(item)

    elif ch == 2:
        item = input("Enter item to remove: ")
        obj.remove_item(item)

    elif ch == 3:
        obj.display()

    elif ch == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")