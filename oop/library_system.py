class Book:
    def __init__(self, title, author):
        """Base class constructor for Book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for Book base class."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class for EBook that inherits from Book.
        Adds file_size attribute.
        """
        super().__init__(title, author)  # Initialize base class attributes
        self.file_size = file_size  # Additional attribute for EBook
    
    def __str__(self):
        """String representation for EBook with file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class for PrintBook that inherits from Book.
        Adds page_count attribute.
        """
        super().__init__(title, author)  # Initialize base class attributes
        self.page_count = page_count  # Additional attribute for PrintBook
    
    def __str__(self):
        """String representation for PrintBook with page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library class using composition to manage a collection of books."""
        self.books = []  # List to store book instances (composition)
    
    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library.
        
        Args:
            book: An instance of Book or its subclasses
        """
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def list_books(self):
        """Prints details of all books in the library."""
        print("\n--- Library Collection ---")
        for book in self.books:
            print(book)
        print("--------------------------")
