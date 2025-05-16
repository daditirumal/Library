 

from manager import Manage

def main():
    manage = Manage()

    # Create tables if they don't exist
    print(manage.create_student_table())
    print(manage.create_table())

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. View Books")
        print("4. Add Student")
        print("5. Update Student")
        print("6. View Students")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            author = input("Enter author name: ").strip()
            title = input("Enter book title: ").strip()
            genre = input("Enter book genre: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            result = manage.add_book(title, author, genre, isbn)
            print(result)

        elif choice == "2":
            isbn = input("Enter book ISBN to update: ").strip()
            print("Leave blank if you don't want to update a field.")
            title = input("Enter new title: ").strip() or None
            author = input("Enter new author: ").strip() or None
            genre = input("Enter new genre: ").strip() or None
            status = input("Enter new status (available/borrowed): ").strip() or None
            result = manage.update_book(isbn, title, author, genre, status)
            print(result)

        elif choice == "3":
            books = manage.view_books()
            if isinstance(books, list):
                for book in books:
                    print(book)
            else:
                print(books)

        elif choice == "4":
            try:
                student_id = int(input("Enter student ID: ").strip())
                name = input("Enter student name: ").strip()
                section = input("Enter student section: ").strip()
                result = manage.add_student(student_id, name, section)
                print(result)
            except ValueError:
                print("Invalid input for student ID.")

        elif choice == "5":
            try:
                student_id = int(input("Enter student ID to update: ").strip())
                print("Leave blank if you don't want to update a field.")
                name = input("Enter new name: ").strip() or None
                section = input("Enter new section: ").strip() or None
                result = manage.update_student(student_id, name, section)
                print(result)
            except ValueError:
                print("Invalid input for student ID.")

        elif choice == "6":
            students = manage.view_students()
            if isinstance(students, list):
                for student in students:
                    print(student)
            else:
                print(students)

        elif choice == "7":
            try:
                student_id = int(input("Enter your student ID: ").strip())
                isbn = input("Enter ISBN of the book to borrow: ").strip()
                result = manage.borrow_book(student_id, isbn)
                print(result)
            except ValueError:
                print("Invalid input for student ID.")

        elif choice == "8":
            try:
                student_id = int(input("Enter your student ID: ").strip())
                isbn = input("Enter ISBN of the book to return: ").strip()
                result = manage.return_book(student_id, isbn)
                print(result)
            except ValueError:
                print("Invalid input for student ID.")

        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
