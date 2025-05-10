import sqlite3
import ***  
conn = sqlite3.connect("libraryDB.db")

cursor = conn.cursor()
class libraryDB:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        Student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')
def insert_book(self, title, author, genre, availability='available'):
    self.cursor.execute('''
        INSERT INTO books (title, author, genre, availability)
        VALUES (?, ?, ?, ?)
    ''', (title, author, genre, availability))
    self.conn.commit()
library = libraryDB()