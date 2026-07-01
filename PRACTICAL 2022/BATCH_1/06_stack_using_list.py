# -------------------------------------------------------------
# Question 6
# Write a Python program to simulate stack data structure
# using lists. Include standard stack operations like
# push(), pop(), peek() and is_empty().
# -------------------------------------------------------------

# Create an empty stack
stack = []

# Function to push an element
def push():
    item = input("Enter element to push: ")
    stack.append(item)
    print(item, "pushed into stack.")

# Function to pop an element
def pop():
    if is_empty():
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

# Function to peek the top element
def peek():
    if is_empty():
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

# Function to check whether stack is empty
def is_empty():
    return len(stack) == 0

# Display all elements
def display():
    if is_empty():
        print("Stack is empty.")
    else:
        print("Stack =", stack)

# Menu-driven program
while True:

    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check Empty")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        if is_empty():
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    elif choice == 5:
        display()

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")