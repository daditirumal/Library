#exception handlers

from manager import Manage   
from database import LibraryDB

def main():
    manage_db = Manage()  

    while True:
        print("\nLibrary Database")
        print("1. Add Book")
        print("2. Update Book")
        print("3. View Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":  # Add a book
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            isbn = input("Enter ISBN: ")
            status = input("Enter status (Available): ")

            result = manage_db.add_book(title, author, genre, isbn, status)
            print(result)

        elif choice == "2":  # Update a book
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (optional): ")
            author = input("Enter new author (optional): ")
            genre = input("Enter new genre (optional): ")
            status = input("Enter new status (optional): ")

            result = manage_db.update_book(isbn, title, author, genre, status)
            print(result)

        elif choice == "3":  # View books
            result = manage_db.view_books()
            if isinstance(result, list):
                for book in result:
                    print(book)
            else:
                print(result)

        elif choice == "4":  # Exit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
