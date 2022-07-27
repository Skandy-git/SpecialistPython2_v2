class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        return f'{self.name[0]}. {self.surname}'


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        return f'"{self.name}" author:{self.author.short_name()} publish:{self.year} год'


author = Author("Александр", "Пушкин")
book = Book("Капитанская дочка", author, 1836, 160)

print(book.to_str())
