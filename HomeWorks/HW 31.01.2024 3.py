# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.__name = name
        self.__year = year
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def get_year(self):
        return self.__year

    def set_year(self, y):
        self.__year = y

    def get_country(self):
        return self.__country

    def set_country(self, c):
        self.__country = c

    def get_city(self):
        return self.__city

    def set_city(self, c):
        self.__city = c

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, c):
        self.__capacity =c

colosseum = Stadium('The Colloseum', '80', 'Italy', 'Rome', '> 50000')

print(colosseum.get_country())
colosseum.set_country('Roman Empire')
print(colosseum.get_country())