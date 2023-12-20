# Задание 4
# Вывести на экран ромб из звездочек.

while True:
    size = int(input('Введите сторону ромба\nНажмите "0" для выхода\n>>>'))
    if size == 0:
        break
    else:
        for i in range(1, size + 1):
            print(' ' * (size - i) + '* ' * i + ' ' * (size - i))
        for i in range(size - 1, 0, -1):
            print(' ' * (size - i) + '* ' * i + ' ' * (size - i))