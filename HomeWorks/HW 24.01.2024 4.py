# Задание 4
# Напишитефункцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.


def min_number(num1, num2, num3, num4, num5):
    numbers = [num1, num2, num3, num4, num5]
    minimum = 99999999
    for i in numbers:
        if i <= minimum:
            minimum = i
    return minimum


print(min_number(-3, 0, 12, -14, 100), '\n\n')
