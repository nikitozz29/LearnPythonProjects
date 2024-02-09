# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


class Money:
    __whole_part = 0
    __penny = 0

    def get_sum(self):
        print(f'You have {self.__whole_part},{self.__penny} money')

    def set_whole_part(self):
        self.__whole_part = int(input('How many whole biils? >> '))

    def set_penny(self):
        self.__penny = int(input('How many penny? >> '))


money = Money()
money.set_whole_part()
money.set_penny()
money.get_sum()