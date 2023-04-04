# Exercise03

# 1
def count_vowels(text):
    if not isinstance(text, str):
        return 42
    vowels = "aAeEiIoOuU"
    count = 0
    for character in text:
        if character in vowels:
            count += 1
    return count


result = count_vowels(23)
print(result)

# 2
def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    else:
        count = 0
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                count += 1
        return count


result = hamming('cat', 'kat')
print(result)

# 3
class Vehicle:

    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def __str__(self):
        pass

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"

my_car = Car("blue", "gasoline", 4)
print(my_car)
my_bus = Bus("yellow", "diesel", 160)
print(my_bus)

# 4
class Book:
    def __init__(self, name, author):
        self.name = name
        self. author = author

    def __str__(self):
        return f"{self.name}, {self.author}"

book1 = Book("Dave", "Raphaela Edelbauer")
print(book1)

# 5
class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)

    def books_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book.name)
        return author_books

    def get_books(self):
        all_books = []
        for book in self.books:
            all_books.append(book.name)
        return all_books

    def clear_shelf(self):
        self.books = []

book1 = Book("Pride and Prejudice", "Jane Austen")
book2 = Book("It", "Stephen King")
book3 = Book ("The Adventures of Huckleberry Finn", "Mark Twain")

bookshelf = BookShelf()
bookshelf.add_book_list([book1, book2, book3, 32, "Hello World"])
all_books = bookshelf.get_books()
print("All books:", all_books)

author_books = bookshelf.books_by_author("Jane Austen")
print("Books by Jane Austen:", author_books)

