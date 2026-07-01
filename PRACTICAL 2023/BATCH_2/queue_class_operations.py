# -------------------------------------------------------------
# Question:
# Write a Python program to create a class representing a Queue
# data structure. Then create methods for the following
# operations:
#
# (a) enqueue()
# (b) dequeue()
# (c) is_empty()
# -------------------------------------------------------------

class Queue:

    # Constructor
    def __init__(self):
        self.queue = []

    # Insert an element into the queue
    def enqueue(self, item):

        self.queue.append(item)

        print(item, "inserted into the queue.")

    # Delete an element from the queue
    def dequeue(self):

        if self.is_empty():
            print("Queue Underflow (Queue is Empty)")
        else:
            item = self.queue.pop(0)
            print(item, "deleted from the queue.")

    # Check whether the queue is empty
    def is_empty(self):

        return len(self.queue) == 0

    # Display the queue
    def display(self):

        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Queue:", self.queue)


# Create Queue object
q = Queue()

# Menu-driven program
while True:

    print("\n------ Queue Menu ------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check Empty")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = input("Enter element: ")
        q.enqueue(value)

    elif choice == 2:

        q.dequeue()

    elif choice == 3:

        if q.is_empty():
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    elif choice == 4:

        q.display()

    elif choice == 5:

        print("Program Ended.")
        break

    else:

        print("Invalid Choice! Please try again.")