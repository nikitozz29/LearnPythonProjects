# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

class TempConverter:
    count = 0

    @staticmethod
    def fahrenheit_to_celsium():
        temp = float(input('Enter temperature in Fahrenheit >> '))
        TempConverter.count += 1
        print(f'Temperature is {(temp - 32) * (5 / 9)} in Celsium.')

    @staticmethod
    def celsium_to_fahrenheit():
        temp = float(input('Enter temperature in Celsium >> '))
        TempConverter.count += 1
        print(f'Temperature is {temp * 1.8 + 32} in Fahrenheit.')

    @staticmethod
    def convert_counter():
        return TempConverter.count


temp_converter = TempConverter()

temp_converter.fahrenheit_to_celsium()
temp_converter.celsium_to_fahrenheit()
print(temp_converter.convert_counter())