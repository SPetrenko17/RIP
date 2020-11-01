class Book:
    # книга
    def __init__(self, id, title, pages, book_store_id):
        self.id = id
        self.title = title
        self.pages = pages
        self.book_store_id = book_store_id


class BookStore:
    # магазин
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookInBStore:
    # книги магазина для реализации связи
    # многие-ко-многим
    def __init__(self, store_id, book_id):
        self.store_id = store_id
        self.book_id = book_id
