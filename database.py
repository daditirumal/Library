import sqlite3

class LibraryDB:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def create_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS books')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL,
                genre TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()
        print("table 'books' created")
        
    def insert_book(self, author, title, gener, isbn , status ="available"):
        self.cursor.execute('''
            INSERT INTO books (author, title, status, gener, isbn)
            VALUES (?, ? , ? , ? , ?)
            ''', (author, title, status, gener, isbn))
        self.conn.commit()
        print(f"BOOK '{title}' added to library")
    def update_book_info(self, isbn, title=None, author=None, genre=None, status=None):
        # Update book details using ISBN
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
            print("No fields to update.")
            return

        values.append(isbn)
        sql = f'''
            UPDATE books
            SET {', '.join(updates)}
            WHERE isbn = ?
        '''
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(f"Book info updated for ISBN {isbn}.")

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found in the database.")


        if _name_ == "_main_":
         db = LibraryDB()

    
        
         db.insert_book("Python 101", "Michael Driscoll", "Programming", "9781234567890")
         db.insert_book("Learning SQL", "John", "Programming", "9780987654321", "Available")

   
         db.update_book_info("9781234567890", author="M. Driscoll", status="Issued")

    
         db.view_books()