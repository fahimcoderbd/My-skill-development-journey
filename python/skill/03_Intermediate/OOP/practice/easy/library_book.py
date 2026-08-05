class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def display(self):
        status = "Available" if self.available else "Borrowed"

        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Status: {status}"
        )

    def borrow(self):
        if not self.available:
            return "❌ Can't borrow twice."

        self.available = False
        return f"✅ '{self.title}' borrowed successfully."

    def return_book(self):
        if self.available:
            return "❌ This book is already available."

        self.available = True
        return f"✅ '{self.title}' returned successfully."


# Testing
book1 = Book("Atomic Habits", "James Clear")

print(book1.display())
print()

print(book1.borrow())
print(book1.borrow())      # Can't borrow twice
print()

print(book1.return_book())
print(book1.return_book()) # Already available
print()

print(book1.display())