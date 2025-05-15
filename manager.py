 

from database import LibraryDB
from model import Book, Student

class Manage:
    def __init__(self):
        self.db = LibraryDB()

    # Book methods
    def add_book(self, title, author, genre, isbn, status="available"):
        try:
            result = self.db.insert_book(author, title, genre, isbn, status)
            return result
        except Exception as e:
            return f"Error adding book: {str(e)}"

    def update_book(self, isbn, title=None, author=None, genre=None, status=None):
        try:
            result = self.db.update_book(isbn, title, author, genre, status)
            return result
        except Exception as e:
            return f"Error updating book: {str(e)}"

    def view_books(self):
        try:
            return self.db.view_books()
        except Exception as e:
            return f"Error retrieving books: {str(e)}"

    def create_table(self):
        try:
            return self.db.create_table()
        except Exception as e:
            return f"Error creating books table: {str(e)}"

    # Student methods
    def create_student_table(self):
        try:
            return self.db.create_student_table()
        except Exception as e:
            return f"Error creating student table: {str(e)}"

    def add_student(self, student_id, name, section):
        try:
            return self.db.insert_student(student_id, name, section)
        except Exception as e:
            return f"Error adding student: {str(e)}"

    def update_student(self, student_id, name=None, section=None):
        try:
            return self.db.update_student(student_id, name, section)
        except Exception as e:
            return f"Error updating student: {str(e)}"

    def view_students(self):
        try:
            return self.db.view_students()
        except Exception as e:
            return f"Error retrieving students: {str(e)}"

    def borrow_book(self, student_id, isbn):
        try:
            # Check if student exists
            students = self.db.view_students()
            student_ids = [s[0] for s in students] if isinstance(students, list) else []

            if student_id not in student_ids:
                # Student does not exist, prompt to add student
                print("Student ID not found. Please provide student details to add.")
                name = input("Enter student name: ").strip()
                section = input("Enter student section: ").strip()
                add_result = self.add_student(student_id, name, section)
                print(add_result)

            # Now proceed to borrow
            result = self.db.borrow_book(student_id, isbn)
            return result
        except Exception as e:
            return f"Error borrowing book: {str(e)}"

    def return_book(self, student_id, isbn):
        try:
            # Check if student exists
            students = self.db.view_students()
            student_ids = [s[0] for s in students] if isinstance(students, list) else []

            if student_id not in student_ids:
                # Student does not exist, prompt to add student
                print("Student ID not found. Please provide student details to add.")
                name = input("Enter student name: ").strip()
                section = input("Enter student section: ").strip()
                add_result = self.add_student(student_id, name, section)
                print(add_result)

             
            result = self.db.return_book(student_id, isbn)
            return result
        except Exception as e:
            return f"Error returning book: {str(e)}"
