#!/usr/bin/env python3
"""
Array Operations Program
Demonstrates basic array (list) operations: insert, delete, search, display, update, etc.
"""

def display_menu():
    print("\n===== ARRAY OPERATIONS =====")
    print("1. Create / Initialize Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Update Element")
    print("6. Display Array")
    print("7. Sort Array")
    print("8. Reverse Array")
    print("9. Get Length")
    print("0. Exit")
    print("============================")

def main():
    arr = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            n = int(input("Enter number of elements: "))
            arr = []
            for i in range(n):
                val = input(f"Enter element {i+1}: ")
                # Try to convert to int if possible, else keep as string
                try:
                    arr.append(int(val))
                except ValueError:
                    arr.append(val)
            print("Array created successfully!")

        elif choice == "2":
            if not arr and input("Array is empty. Create first? (y/n): ").lower() != 'y':
                continue
            val = input("Enter element to insert: ")
            try:
                val = int(val)
            except ValueError:
                pass
            pos = input("Enter position (0-based index, or press Enter to append): ").strip()
            if pos == "":
                arr.append(val)
                print(f"Appended {val}")
            else:
                pos = int(pos)
                if 0 <= pos <= len(arr):
                    arr.insert(pos, val)
                    print(f"Inserted {val} at index {pos}")
                else:
                    print("Invalid position!")

        elif choice == "3":
            if not arr:
                print("Array is empty!")
                continue
            print("Current array:", arr)
            mode = input("Delete by (1) value or (2) index? ").strip()
            if mode == "1":
                val = input("Enter value to delete: ")
                try:
                    val = int(val)
                except ValueError:
                    pass
                if val in arr:
                    arr.remove(val)
                    print(f"Deleted first occurrence of {val}")
                else:
                    print("Value not found!")
            elif mode == "2":
                idx = int(input("Enter index to delete: "))
                if 0 <= idx < len(arr):
                    removed = arr.pop(idx)
                    print(f"Deleted {removed} from index {idx}")
                else:
                    print("Invalid index!")

        elif choice == "4":
            if not arr:
                print("Array is empty!")
                continue
            val = input("Enter value to search: ")
            try:
                val = int(val)
            except ValueError:
                pass
            if val in arr:
                indices = [i for i, x in enumerate(arr) if x == val]
                print(f"Found at index(es): {indices}")
            else:
                print("Element not found!")

        elif choice == "5":
            if not arr:
                print("Array is empty!")
                continue
            print("Current array:", arr)
            idx = int(input("Enter index to update: "))
            if 0 <= idx < len(arr):
                new_val = input("Enter new value: ")
                try:
                    new_val = int(new_val)
                except ValueError:
                    pass
                old = arr[idx]
                arr[idx] = new_val
                print(f"Updated index {idx}: {old} -> {new_val}")
            else:
                print("Invalid index!")

        elif choice == "6":
            if not arr:
                print("Array is empty!")
            else:
                print("Array contents:", arr)

        elif choice == "7":
            if not arr:
                print("Array is empty!")
            else:
                try:
                    arr.sort()
                    print("Array sorted (ascending):", arr)
                except TypeError:
                    print("Cannot sort mixed types. Sorting as strings...")
                    arr = sorted(arr, key=str)
                    print("Array sorted:", arr)

        elif choice == "8":
            if not arr:
                print("Array is empty!")
            else:
                arr.reverse()
                print("Array reversed:", arr)

        elif choice == "9":
            print(f"Length of array: {len(arr)}")

        elif choice == "0":
            print("Exiting Array Operations. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
