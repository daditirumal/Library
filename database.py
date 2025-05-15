 

import sqlite3

class LibraryDB:
    def __init__(self, db_name="library.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except:
            print("Could not connect to the database.")

    def create_table(self):
        try:
            self.cursor.execute('DROP TABLE IF EXISTS books')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER,
                    author TEXT NOT NULL,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    isbn TEXT NOT NULL UNIQUE,
                    PRIMARY KEY(isbn),
                    FOREIGN KEY (id) REFERENCES students(id)
                )
            ''')
            self.conn.commit()
            return "Table 'books' created."
        except:
            return "Error creating book table."

    def create_student_table(self):
        try:
            self.cursor.execute('DROP TABLE IF EXISTS students')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    section TEXT NOT NULL
                )
            ''')
            self.conn.commit()
            return "Table 'students' created."
        except:
            return "Error creating student table."

    def insert_book(self, author, title, genre, isbn, status="available"):
        try:
            self.cursor.execute('''
                INSERT INTO books (id, author, title, status, genre, isbn)
                VALUES (NULL, ?, ?, ?, ?, ?)
            ''', (author, title, status, genre, isbn))
            self.conn.commit()
            return f"Book '{title}' added to library."
        except:
            return "Error adding the book. The ISBN might already exist."

    def update_book(self, isbn, title=None, author=None, genre=None, status=None):
        try:
            updates = []
            values = []

            if title:
                updates.append("title = ?")
                values.append(title)
            if author:
                updates.append("author = ?")
                values.append(author)
            if genre:
                updates.append("genre = ?")
                values.append(genre)
            if status:
                updates.append("status = ?")
                values.append(status)

            if not updates:
                return "No fields to update."

            values.append(isbn)
            sql = f'''
                UPDATE books
                SET {', '.join(updates)}
                WHERE isbn = ?
            '''
            self.cursor.execute(sql, values)
            self.conn.commit()
            return f"Book info updated for ISBN {isbn}."
        except:
            return "Error updating book. Please check the ISBN and values."

    def view_books(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            books = self.cursor.fetchall()
            return books if books else "No books found in the database."
        except:
            return "Error retrieving books."

    def insert_student(self, id, name, section):
        try:
            self.cursor.execute('''
                INSERT INTO students (id, name, section)
                VALUES (?, ?, ?)
            ''', (id, name, section))
            self.conn.commit()
            return f"Student '{name}' added."
        except:
            return "Error adding student. ID might already exist."

    def update_student(self, id, name=None, section=None):
        try:
            updates = []
            values = []

            if name:
                updates.append("name = ?")
                values.append(name)
            if section:
                updates.append("section = ?")
                values.append(section)

            if not updates:
                return "No fields to update."

            values.append(id)
            sql = f'''
                UPDATE students
                SET {', '.join(updates)}
                WHERE id = ?
            '''
            self.cursor.execute(sql, values)
            self.conn.commit()
            return f"Student info updated for ID {id}."
        except:
            return "Error updating student. Please check the ID."

    def view_students(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            students = self.cursor.fetchall()
            return students if students else "No students found in the database."
        except:
            return "Error retrieving students."

    def borrow_book(self, student_id, isbn):
        try:
            # Check borrow count for student
            self.cursor.execute("SELECT COUNT(*) FROM books WHERE id = ?", (student_id,))
            count = self.cursor.fetchone()[0]
            if count >= 3:
                return "Borrowing limit reached (3 books)."

            # Check book availability
            self.cursor.execute("SELECT status FROM books WHERE isbn = ?", (isbn,))
            result = self.cursor.fetchone()
            if not result:
                return "Book not found."
            if result[0].lower() != "available":
                return "Book is not available."

            # Update book status and assign to student
            self.cursor.execute("""
                UPDATE books SET status = 'borrowed', id = ? WHERE isbn = ?
            """, (student_id, isbn))
            self.conn.commit()
            return f"Book with ISBN {isbn} issued to student ID {student_id}."
        except:
            return "Error processing book borrowing."

    def return_book(self, student_id, isbn):
        try:
            # Check if book is borrowed by this student
            self.cursor.execute("""
                SELECT * FROM books WHERE isbn = ? AND id = ?
            """, (isbn, student_id))
            result = self.cursor.fetchone()
            if not result:
                return "This book is not borrowed by this student."

            # Update book status and remove student assignment
            self.cursor.execute("""
                UPDATE books SET status = 'available', id = NULL WHERE isbn = ?
            """, (isbn,))
            self.conn.commit()
            return f"Book with ISBN {isbn} returned by student ID {student_id}."
        except:
            return "Error processing book return."
