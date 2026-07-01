# -------------------------------------------------------------
# Question 8
# Write a Python program to simulate stack operations
# using list (PUSH, POP, PEEP).
# Also check overflow and underflow conditions.
# -------------------------------------------------------------

MAX = 5
stack = []

def push():

    if len(stack) == MAX:
        print("Stack Overflow")

    else:
        item = input("Enter element: ")
        stack.append(item)
        print("Element Pushed")


def pop():

    if len(stack) == 0:
        print("Stack Underflow")

    else:
        print("Deleted:", stack.pop())


def peep():

    if len(stack) == 0:
        print("Stack Empty")

    else:
        print("Top Element:", stack[-1])


while True:

    print("\n1.Push")
    print("2.Pop")
    print("3.Peep")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peep()

    elif choice == 4:
        print(stack)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")