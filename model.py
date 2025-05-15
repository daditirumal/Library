class Book:
    def __init__(self, author, title, genre, isbn, status="available"):
        self.author = author
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.status = status

class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
