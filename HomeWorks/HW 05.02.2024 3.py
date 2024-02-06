# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class SiConverter:

    @staticmethod
    def inch_to_si(inch):
        print(f'{inch} inches is {inch * 0.0254} metres')
    @staticmethod
    def metres_to_inch(metres):
        print(f'{metres} metres is {metres / 0.0254} inches')
    @staticmethod
    def foot_to_metres(foot):
        print(f'{foot} foots is {foot * 0.3048} metres')
    @staticmethod
    def metres_to_foot(metres):
        print(f'{metres} metres is {metres / 0.3048} foots')
    @staticmethod
    def hand_to_metres(hand):
        print(f'{hand} hands is {hand * 0.1016} metres')
    @staticmethod
    def metres_to_hand(metres):
        print(f'{metres} metres is {metres / 0.1016} hands')
    @staticmethod
    def yard_to_metres(yard):
        print(f'{yard} yards is {yard * 0.9144} metres')
    @staticmethod
    def metres_to_yard(metres):
        print(f'{metres} metres is {metres / 0.9144} yards')
    @staticmethod
    def furlong_to_metres(furlong):
        print(f'{furlong} furlongs is {furlong * 201} metres')
    @staticmethod
    def metres_to_furlong(metres):
        print(f'{metres} metres is {metres / 201} furlongs')
    @staticmethod
    def mile_to_metres(mile):
        print(f'{mile} miles is {mile * 1609} metres')
    @staticmethod
    def metres_to_miles(metres):
        print(f'{metres} metres is {metres / 1609} miles')

SiConverter.inch_to_si(5)
SiConverter.metres_to_inch(5)
SiConverter.foot_to_metres(5)
SiConverter.metres_to_foot(5)
SiConverter.hand_to_metres(5)
SiConverter.metres_to_hand(5)
SiConverter.yard_to_metres(5)
SiConverter.metres_to_yard(5)
SiConverter.furlong_to_metres(5)
SiConverter.metres_to_furlong(5)
SiConverter.mile_to_metres(5)
SiConverter.metres_to_miles(5)