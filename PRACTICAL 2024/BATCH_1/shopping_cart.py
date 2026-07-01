# Program 4
# Write a menu driven Python program to create a Shopping Cart class.
class ShoppingCart:
    def __init__(self):
         self.cart = {}#dictionary

    def display(self):
        if(len(self.cart)==0):
            print("Empty..")
        else:
            print("Item in shopping cart:")
            print("Item\tPrice")
            for item,price in self.cart.items():
                print(item,":",price)

    def add(self,item,price):
        self.cart[item]=price
        print(f"{item} added successfully.")

    def remove(self,val):
        if val in self.cart:
            self.cart.pop(val)
            print(f"{val} removed successfully.")
        else:
            print("Item not found")

    def calculate(self):
        total=sum(self.cart.values())
        print("Total price is:",total)


s1=ShoppingCart()
while True:
    print("----MENU----")
    print("1.ADD ITEM")
    print("2.REMOVE ITEM")
    print("3.DISPLAY")
    print("4.CALCULATE PRICE")
    print("5.EXIT")
    choice=int(input("Enter your choice:"))

    if choice==1:
        s1.add(input("Enter the item:"),int(input("Enter the price:")))
    elif choice==2:
        s1.remove(input("Enter the remove val:"))
    elif choice==3:
        s1.display()
    elif choice==4:
        s1.calculate()
    elif choice==5:
        print("Thank You!")
        break
    else:
        print("Invalid input...")