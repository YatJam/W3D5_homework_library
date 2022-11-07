from models.book import Book

book1 = Book("9782451127892", "The Curse of Jam", "Count Jamula", "Healthy Living", "A11 K11", True)
book2 = Book("9784443278569", "Coping with a cold", "Alotta Lemsip", "True Crime", "D44A", True)
book3 = Book("9781003765528", "Not coping with a cold", "Jums Yotts", "Horror", "F13 C3", False)
book4 = Book("9783667712894", "Memoirs of a sick-free life", "Jimmy Yutts", "Biography", "U67 D4", False)

library = [book1, book2, book3, book4]

def add_new_book(new_book):
    library.append(new_book)

def delete_book(book_title):
    book_to_delete = None
    for book in library:
        if book.title == book_title:
            book_to_delete = book

    library.remove(book_to_delete)