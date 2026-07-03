class Test:
    def __init__(self,num):
        self.x=0
        self.y=0
        self.num=num

    def input(self):
        self.x=int(input("Enter the num 1:"))
        self.y=int(input("Enter the num 2:"))

    def display(self):
        print("The number is:",self.num)
        print("The number 1 is:",self.x)
        print("The number 2 is:",self.y)

num=int(input("Enter the number:"))
t1=Test(num)
t1.display()
t1.input()
t1.display()

# Enter the number:100
# The number is: 100
# The number 1 is: 0
# The number 2 is: 0
# Enter the num 1:25
# Enter the num 2:50
# The number is: 100
# The number 1 is: 25
# The number 2 is: 50