# 2. Write a Python program to implement the Stack operations
# (a) Overflow()
# (b) Underflow()
# (c) Push(O
# (d) Pop()

class Stack:
    def __init__(self):
        self.stack = []
    
    # Function to check Overflow
    def Overflow(self):
        if len(self.stack) == size:
            return True
        return False


    # Function to check Underflow
    def Underflow(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.Underflow():
            print("Stack is Empty")
        else:
            print("Popped element is:", self.stack.pop())

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack elements are:")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top element is:", self.stack[-1])

size = int(input("Enter stack size: "))
s1 = Stack()

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Peek")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if s1.Overflow()==True:
            print("Stack is Full")
        else:
            data = int(input("Enter data: "))
            s1.push(data)

    elif choice == 2:
        s1.pop()

    elif choice == 3:
        s1.display()

    elif choice == 4:
        s1.peek()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")