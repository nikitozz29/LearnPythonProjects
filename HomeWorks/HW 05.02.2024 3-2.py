# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Ship:
    def __init__(self, name, displacement):
        self.__name = name
        self.__displacement = displacement

    def get_name(self):
        return self.__name

    def get_displacement(self):
        return self.__displacement


class Frigate(Ship):
    def __init__(self, name, displacement):
        super().__init__(name, displacement)
        self.__name = name
        self.__displacement = displacement
        self.__typo = 'Type - Frigate'

    def get_type(self):
        return self.__typo

    def display_info(self):
        print(f'Name: {self.__name}\nDisplacement: {self.__displacement}\nType: {self.__typo}')


class Destroyer(Ship):
    def __init__(self, name, displacement):
        super().__init__(name, displacement)
        self.__name = name
        self.__displacement = displacement
        self.__typo = 'Type - Destroyer'

    def get_type(self):
        return self.__typo

    def display_info(self):
        print(f'Name: {self.__name}\nDisplacement: {self.__displacement}\nType: {self.__typo}')


class Cruiser(Ship):
    def __init__(self, name, displacement):
        super().__init__(name, displacement)
        self.__name = name
        self.__displacement = displacement
        self.__typo = 'Type - Cruiser'

    def get_type(self):
        return self.__typo

    def display_info(self):
        print(f'Name: {self.__name}\nDisplacement: {self.__displacement}\nType: {self.__typo}')


frigate = Frigate('Duke', 4900)
destroyer = Destroyer('John Paul Johns', 6630)
cruiser = Cruiser('Aurora', 6731)


frigate.display_info()
destroyer.display_info()
cruiser.display_info()