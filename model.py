class Book:
    def __init__(self, name, title, isbn, status="available"):
        self.name = name 
        self.title = title
        self.isbn = isbn   
        self.status = status  

    
    def get_details(self):
        return f"Book: {self.title} by {self.name} (ISBN: {self.isbn}, Status: {self.status})"

if __name__ == "__main__":
    # Creating an object of the Book class
    book = Book(name="Michael Driscoll", title="Python 101", isbn="9781234567890")
    print(book.get_details())
