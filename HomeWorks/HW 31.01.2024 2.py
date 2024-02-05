# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    def __init__(self, name, year, producer, genre, author, price):
        self.__name = name
        self.__year = year
        self.__producer = producer
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def get_year(self):
        return self.__year

    def set_year(self, y):
        self.__year = y

    def get_producer(self):
        return self.__producer

    def set_producer(self, p):
        self.__producer = p

    def get_genre(self):
        return self.__genre

    def set_genre(self, g):
        self.__genre = g

    def get_author(self):
        return self.__author

    def set_color(self, a):
        self.__author = a

    def get_price(self, ):
        return self.__price

    def set_price(self, p):
        self.__price = p


my_book = Book('Dune', '1965', 'Chilton Books', 'Novel', 'Frank Herbert', 1000)

print(my_book.get_genre())
my_book.set_genre('SCI')
print(my_book.get_genre())