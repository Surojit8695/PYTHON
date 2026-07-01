# Double Ended Queue (Deque)

class Deque:
    def __init__(self):
        self.q = []

    # Insert at Front
    def insert_front(self, data):
        self.q.insert(0, data)

    # Insert at Rear
    def insert_rear(self, data):
        self.q.append(data)

    # Delete from Front
    def delete_front(self):
        print("Deleted element is:", self.q.pop(0))

    # Delete from Rear
    def delete_rear(self):
        print("Deleted element is:", self.q.pop())

    # Display Queue
    def display(self):
        for i in self.q:
            print(i, end=" ")
        print()


max = int(input("Enter the size of the queue: "))

q1 = Deque()

front = -1
rear = -1

while True:

    print("\n----- MENU -----")
    print("1. INSERT FRONT")
    print("2. INSERT REAR")
    print("3. DELETE FRONT")
    print("4. DELETE REAR")
    print("5. DISPLAY")
    print("6. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if rear == max - 1:
            print("Queue is Full")

        else:

            data = int(input("Enter the data: "))

            q1.insert_front(data)

            if front == -1:
                front = 0

            rear += 1

    elif choice == 2:

        if rear == max - 1:
            print("Queue is Full")

        else:

            data = int(input("Enter the data: "))

            q1.insert_rear(data)

            if front == -1:
                front = 0

            rear += 1

    elif choice == 3:

        if front == -1:
            print("Queue is Empty")

        else:

            q1.delete_front()

            if front == rear:
                front = -1
                rear = -1
            else:
                rear -= 1

    elif choice == 4:

        if front == -1:
            print("Queue is Empty")

        else:

            q1.delete_rear()

            if front == rear:
                front = -1
                rear = -1
            else:
                rear -= 1

    elif choice == 5:

        if front == -1:
            print("Queue is Empty")

        else:
            print("Queue elements are:")
            q1.display()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")