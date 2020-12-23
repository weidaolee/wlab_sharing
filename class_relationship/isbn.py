
class Book:
    def __init__(self, isbn_number: "", title="", author_set=set()):
        self.isbn = ISBN(isbn_number)
        self.title = title
        self.author_set = author_set


class ISBN:

    def __init__(self, isbn_number):
        if not self.is_legal_isbn_number(isbn_number):
            raise ValueError("Illegal ISBN")

        self.isbn_number = isbn_number

    def get_group_id(self):
        ...

    def get_publisher_id(self):
        ...

    def get_title_id(self):
        ...

    def get_check_digit(self):
        ...

    def is_legal_isbn_number(self, isbn_number):
        is_legal = False
        if len(isbn_number) != 7:
            ...
        else:
            is_legal = True
        return is_legal


class Library:
    def __init__(self, name):
        self.name = name
        self.book_table = {}

    def add_book(self, book):
        self.book_table[book.isbn] = book

    def inquire(self, isbn):
        return self.book_table[isbn]


book = Book("1234567")
