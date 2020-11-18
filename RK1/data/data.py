from ..models.models import Book, BookInBStore, BookStore

# Магазины
stores = [
    BookStore(1, "Chitay-Gorod Store"),
    BookStore(2, "Respublika Store"),
    BookStore(3, "Knigga Store Store"),

    BookStore(4, "BookStore Store"),
    BookStore(5, "BookBridge Store"),
    BookStore(6, "BookMania Store")
]

# Книги
books = [
    Book(1, "Fifty shades of grey", 100, 1),
    Book(2, "Fifty shades of darker", 200, 2),
    Book(3, "Fifty shades freer", 300, 2),
    Book(4, "War and peace", 400, 3),
    Book(5, "Anna Karenina", 500, 3),
    Book(6, "Evgeniy Onegin", 600, 3),
    Book(7, "Book of the dead", 700, 3)
]

books_stores = [
    BookInBStore(1, 1),
    BookInBStore(2, 2),
    BookInBStore(2, 3),
    BookInBStore(3, 4),
    BookInBStore(3, 5),
    BookInBStore(3, 6),
    BookInBStore(3, 7),
    BookInBStore(4, 1),
    BookInBStore(5, 2),
    BookInBStore(5, 3),
    BookInBStore(6, 4),
    BookInBStore(6, 5),
    BookInBStore(6, 6),
    BookInBStore(6, 7),
]

# соединение данных один-ко-многим
one_to_many = [(c.title, c.pages, o.name)
               for o in stores
               for c in books
               if c.book_store_id == o.id]

# соединение данных многие-ко-многим
many_to_many = [(c.title, c.pages, store_name)
                for store_name, store_id, book_id in [(o.name, co.store_id, co.book_id)
                                                      for o in stores
                                                      for co in books_stores
                                                      if o.id == co.store_id]
                for c in books if c.id == book_id]