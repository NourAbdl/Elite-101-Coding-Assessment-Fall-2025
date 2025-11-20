from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books(books):
    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print(f"{book['id']} - {book['title']} by {book['author']}")
    print()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(books, author=None, genre=None):
    author = author.lower() if author else None
    genre = genre.lower() if genre else None

    results = []
    for book in books:
        if author and author in book["author"].lower():
            results.append(book)
        elif genre and genre in book["genre"].lower():
            results.append(book)

    return results

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                book["due_date"] = (datetime.now() + timedelta(weeks=2)).strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(f"{book['title']} checked out! Due: {book['due_date']}")
            else:
                print(f"{book['title']} is already checked out.")
            return

    print("Book not found.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            book["due_date"] = None
            print(f"{book['title']} has been returned.")
            return

    print("Book not found.")


def list_overdue_books(books):
    print("\nOverdue Books:")
    today = datetime.now().date()

    for book in books:
        if not book["available"] and book["due_date"]:
            due = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due < today:
                print(f"{book['id']} - {book['title']} (Due: {book['due_date']})")
    print()

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
def show_menu():
    print("======== Library Menu ========")
    print("1. View available books")
    print("2. Search books by author")
    print("3. Search books by genre")
    print("4. Checkout a book")
    print("5. Return a book")
    print("6. List overdue books")
    print("7. Quit")
    print("------------------------------")
    def run_library(books):
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_available_books(books)

        elif choice == "2":
            name = input("Enter author name: ")
            results = search_books(books, author=name)
            print("\nSearch Results:")
            for book in results:
                print(f"{book['id']} - {book['title']}")

        elif choice == "3":
            g = input("Enter genre: ")
            results = search_books(books, genre=g)
            print("\nSearch Results:")
            for book in results:
                print(f"{book['id']} - {book['title']}")

        elif choice == "4":
            book_id = input("Enter book ID to checkout: ")
            checkout_book(books, book_id)

        elif choice == "5":
            book_id = input("Enter book ID to return: ")
            return_book(books, book_id)

        elif choice == "6":
            list_overdue_books(books)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
