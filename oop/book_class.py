# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Initializes a Book instance with the given title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a user-friendly string representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
