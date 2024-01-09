# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

import random

digits = [random.randint(-100, 100) for i in range(50)]
print(digits)

min_value = min(digits)
max_value = max(digits)
count_negative = 0
count_positive = 0
count_zero = 0

for i in range(len(digits)):
    if digits[i] < 0:
        count_negative += 1
    if digits[i] > 0:
        count_positive += 1
    if digits[i] == 0:
        count_zero += 1

print('Минимальное ', min_value)
print('Максимальное ', max_value)
print('Отрицательных ', count_negative)
print('Положительных ', count_positive)
print('Нулей ', count_zero)