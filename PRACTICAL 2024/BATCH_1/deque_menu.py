# Program 6
# Write a Python program to implement Deque using menu driven approach.

from collections import deque

dq = deque()

while True:

    print("\n1.Insert Front")
    print("2.Insert Rear")
    print("3.Delete Front")
    print("4.Delete Rear")
    print("5.Display")
    print("6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        dq.appendleft(x)

    elif ch == 2:
        x = int(input("Enter element: "))
        dq.append(x)

    elif ch == 3:
        if dq:
            print("Deleted:", dq.popleft())
        else:
            print("Deque Empty")

    elif ch == 4:
        if dq:
            print("Deleted:", dq.pop())
        else:
            print("Deque Empty")

    elif ch == 5:
        print(list(dq))

    elif ch == 6:
        break

    else:
        print("Invalid Choice")