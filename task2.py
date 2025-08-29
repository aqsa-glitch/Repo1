

import json
import os

FILE_NAME = "books.json"


def load_data():
    """Load the books list from JSON file; return empty list if file doesn't exist or is empty/corrupt."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_data(books):
    """Save the list of book dictionaries to JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def input_int(prompt):
    """Safely read an integer from input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Please enter a valid number.")


def find_book_by_id(books, book_id):
    """Return (index, book_dict) if found else (None, None)."""
    for idx, b in enumerate(books):
        if str(b.get("id")) == str(book_id):
            return idx, b
    return None, None


def add_book(books):
    print("\n=== Add New Book ===")
    book_id = input("Enter Book ID: ").strip()
    # Prevent duplicate IDs
    _, existing = find_book_by_id(books, book_id)
    if existing:
        print(" A book with this ID already exists.")
        return

    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    quantity = input_int("Enter Quantity (number): ")
    if quantity < 0:
        print(" Quantity cannot be negative.")
        return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }
    books.append(book)
    save_data(books)
    print(" Book added and saved successfully!")


def view_books(books):
    print("\n=== All Available Books ===")
    if not books:
        print("No books found.")
        return
    for b in books:
        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']} | Quantity: {b['quantity']}")


def borrow_book(books):
    print("\n=== Borrow a Book ===")
    book_id = input("Enter Book ID to borrow: ").strip()
    idx, book = find_book_by_id(books, book_id)
    if book is None:
        print(" Book not found.")
        return

    if book["quantity"] > 0:
        book["quantity"] -= 1
        books[idx] = book
        save_data(books)
        print(f" Borrowed: {book['title']} (Remaining: {book['quantity']})")
    else:
        print(" Book is currently not available (quantity is 0).")


def return_book(books):
    print("\n=== Return a Book ===")
    book_id = input("Enter Book ID to return: ").strip()
    idx, book = find_book_by_id(books, book_id)
    if book is None:
        print(" Book not found.")
        return
    book["quantity"] += 1
    books[idx] = book
    save_data(books)
    print(f" Returned: {book['title']} (Now available: {book['quantity']})")


def main():
    books = load_data()
    while True:
        print("\n===== Mini Library Management System =====")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print(" Exiting... (Data saved to books.json)")
            break
        else:
            print(" Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
