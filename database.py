import sqlite3
#add student database
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
        return "Table 'books' created."
        
    def insert_book(self, author, title, genre, isbn, status="available"):
        self.cursor.execute('''
            INSERT INTO books (author, title, status, genre, isbn)
            VALUES (?, ?, ?, ?, ?)
        ''', (author, title, status, genre, isbn))
        self.conn.commit()
        return f"Book '{title}' added to library."
    
    def update_book_info(self, isbn, title=None, author=None, genre=None, status=None):
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
    
    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        if books:
            return books
        else:
            return "No books found in the database."


if __name__ == "__main__":
    db = LibraryDB()

    print(db.create_table())
    print(db.insert_book("Michael Driscoll", "Python 101", "Programming", "9781234567890"))
    print(db.insert_book("John", "Learning SQL", "Programming", "9780987654321", "Available"))
    print(db.update_book_info("9781234567890", author="M. Driscoll", status="Issued"))
    print(db.view_books())
