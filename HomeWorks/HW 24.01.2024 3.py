# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


def square(length, symbol, full: bool):
    if full:
        for i in range(0, length):
            for j in range(0, length):
                print(symbol, end='')
            print('')
    else:
        print(symbol * length, end='')
        print()
        for i in range(0, length - 2):
            print(symbol + ' ' * (length - 2) + symbol)
        print(symbol * length, end='')


square(5, '&', True)
print('\n')
square(5, '&', False)
print('\n\n')
