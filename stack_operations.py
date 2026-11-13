#!/usr/bin/env python3
"""
Stack Operations Program
Implements a Stack using a Python list (LIFO - Last In First Out)
Operations: Push, Pop, Peek, isEmpty, Display, Size
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from empty stack.")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        print(f"Top element: {self.items[-1]}")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack (top -> bottom):", list(reversed(self.items)))
            print("Internal representation (bottom -> top):", self.items)

def display_menu():
    print("\n===== STACK OPERATIONS =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek (Top)")
    print("4. Display Stack")
    print("5. Check if Empty")
    print("6. Get Size")
    print("0. Exit")
    print("============================")

def main():
    stack = Stack()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = input("Enter value to push: ")
            try:
                val = int(val)
            except ValueError:
                pass
            stack.push(val)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.peek()

        elif choice == "4":
            stack.display()

        elif choice == "5":
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")

        elif choice == "6":
            print(f"Current size: {stack.size()}")

        elif choice == "0":
            print("Exiting Stack Operations. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
