# Program 5
# Write a Python program to implement Queue operations:
# createQueue(), enqueue(), dequeue()

queue = []

def createQueue():
    global queue
    queue = []
    print("Queue Created")

def enqueue():
    item = int(input("Enter element: "))
    queue.append(item)
    print("Inserted Successfully")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted:", queue.pop(0))

while True:

    print("\n1.Create Queue")
    print("2.Enqueue")
    print("3.Dequeue")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        createQueue()

    elif choice == 2:
        enqueue()

    elif choice == 3:
        dequeue()

    elif choice == 4:
        print(queue)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")