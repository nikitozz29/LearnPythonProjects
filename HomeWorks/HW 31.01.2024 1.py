# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса

class Auto:
    def __init__(self, model, year, producer, driver_value, color, price):
        self.__model = model
        self.__year = year
        self.__producer = producer
        self.__driver_value = driver_value
        self.__color = color
        self.__price = price

    def get_model(self):
        return self.__model

    def set_model(self, m):
        self.__model = m

    def get_year(self):
        return self.__year

    def set_year(self, y):
        self.__year = y

    def get_producer(self):
        return self.__producer

    def set_producer(self, p):
        self.__producer = p

    def get_driver_value(self):
        return self.__driver_value

    def set_driver_value(self, d):
        self.__driver_value = d

    def get_color(self):
        return self.__color

    def set_color(self, c):
        self.__color = c

    def get_price(self, ):
        return self.__price

    def set_price(self, p):
        self.__price = p


my_car = Auto('Dodge Stratus 2', '2001', 'Daimler - Chrysler', '2.4', 'Wet asphalt', 200000)

print(my_car.get_price())
my_car.set_price(250000)
print(my_car.get_price())

