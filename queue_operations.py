#!/usr/bin/env python3
"""
Queue Operations Program
Implements a Queue using a Python list (FIFO - First In First Out)
Operations: Enqueue, Dequeue, Front, isEmpty, Display, Size
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from empty queue.")
            return None
        item = self.items.pop(0)
        print(f"Dequeued: {item}")
        return item

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.items[0]}")
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue (front -> rear):", self.items)

def display_menu():
    print("\n===== QUEUE OPERATIONS =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front (Peek)")
    print("4. Display Queue")
    print("5. Check if Empty")
    print("6. Get Size")
    print("0. Exit")
    print("============================")

def main():
    queue = Queue()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = input("Enter value to enqueue: ")
            try:
                val = int(val)
            except ValueError:
                pass
            queue.enqueue(val)

        elif choice == "2":
            queue.dequeue()

        elif choice == "3":
            queue.front()

        elif choice == "4":
            queue.display()

        elif choice == "5":
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice == "6":
            print(f"Current size: {queue.size()}")

        elif choice == "0":
            print("Exiting Queue Operations. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
