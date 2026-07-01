# -------------------------------------------------------------
# Question:
# Write a Python class to implement Queue data structure
# with enqueue(), dequeue() and isEmpty() functions.
# -------------------------------------------------------------

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):

        self.queue.append(item)

    def dequeue(self):

        if self.isEmpty():
            print("Queue Underflow")
        else:
            print("Deleted:", self.queue.pop(0))

    def isEmpty(self):

        return len(self.queue) == 0

    def display(self):

        print("Queue:", self.queue)


q = Queue()

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Check Empty")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        item = input("Enter element: ")
        q.enqueue(item)

    elif ch == 2:
        q.dequeue()

    elif ch == 3:
        print(q.isEmpty())

    elif ch == 4:
        q.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")