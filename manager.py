# creating a Manage class that acts like a controller 
# between Book model and the LibraryDB database.

# count - books
# 

from database import LibraryDB 
from model import Book
  
class Manage:
    def __init__(self):
        self.db = LibraryDB() 

    def add_book(self, title, author, genre, isbn, status="available"):
        result_add_book = self.db.insert_book(author, title, genre, isbn, status)
        return result_add_book

    def update_book(self, isbn, title, author, genre, status):
        result_u_book = self.db.update_book(isbn, title, author, genre, status)
        return result_u_book

    def view_books(self):
        result_v_book = self.db.view_books()  # Method to view books
        return result_v_book

    def create_table(self):
        result_dbconnection = self.db.create_table()  # Method to create table
        return result_dbconnection  # "Table 'books' created."
