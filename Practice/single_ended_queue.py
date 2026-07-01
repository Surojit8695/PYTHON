# Linear Queue using C Programming Logic

class Queue:
    def __init__(self):
        self.q = []

    # Insert at Rear
    def enqueue(self, data):
        self.q.append(data)

    # Delete from Front
    def dequeue(self):
        print("Deleted element is:", self.q.pop(0))

    # Display Queue
    def display(self):
        for i in self.q:
            print(i, end=" ")
        print()


max = int(input("Enter the size of the queue: "))

q1 = Queue()

front = -1
rear = -1

while True:

    print("\n----- MENU -----")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if rear == max - 1:
            print("Queue is Full")

        else:

            data = int(input("Enter the data: "))

            if front == -1:
                front = 0

            rear += 1
            q1.enqueue(data)

    elif choice == 2:

        if front == -1:
            print("Queue is Empty")

        else:

            q1.dequeue()

            if front == rear:
                front = -1
                rear = -1
            else:
                front += 1

    elif choice == 3:

        if front == -1:
            print("Queue is Empty")

        else:
            print("Queue elements are:")
            q1.display()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")