# Задание 5
# Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
# Если границы диапазона указаны неправильно требуется
# произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой
# начало диапазона станет равно 13, а конец 33.


a = int(input('Введите начало диапазона >'))
b = int(input('Введите конец диапазона >'))

if a > b:
    c = a
    a = b
    b = c

for i in range(a, b + 1):
    if i % 2 == 1:
        print(i)
