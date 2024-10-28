from abc import ABC, abstractmethod

# Abstract class
class LibraryItem(ABC):
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    @abstractmethod
    def display_details(self):
        pass

    def borrow(self):
        print(f"{self.title} has been borrowed.")

    def return_item(self):
        print(f"{self.title} has been returned.")

# Subclass for Book
class Book(LibraryItem):
    def __init__(self, title, author, publication_date, isbn):
        super().__init__(title, author, publication_date)
        self.isbn = isbn

    def display_details(self):
        print(f"Book Title: {self.title}, Author: {self.author}, "
              f"Publication Date: {self.publication_date}, ISBN: {self.isbn}")

# Subclass for Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, publication_date, issue_no):
        super().__init__(title, author, publication_date)
        self.issue_no = issue_no

    def display_details(self):
        print(f"Magazine Title: {self.title}, Author: {self.author}, "
              f"Publication Date: {self.publication_date}, Issue No: {self.issue_no}")

# Creating objects and calling their methods
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "9780743273565")
magazine = Magazine("National Geographic", "Various", "2023", "202")

book.display_details()
book.borrow()
book.return_item()

magazine.display_details()
magazine.borrow()
magazine.return_item()
