# Задание 1
# В списке целых, заполненном случайными числами
# вычислить:
# Сумму отрицательных чисел;
# Сумму четных чисел;
# Сумму нечетных чисел;
# Произведение элементов с индексами кратными 3;
# Произведение элементов между минимальным и
# максимальным элементом;
# Сумму элементов, находящихся между первым и последним положительными элементами.

import random

numbers = [random.randint(-100, 100) for i in range(20)]
print(numbers)

sum_negative = 0
sum_even = 0
sum_odd = 0
product3 = 1
product_min_max = 1
first_positive_index = 0
last_positive_index = 0
sum_positive = 0

min_value = numbers.index(min(numbers))
max_value = numbers.index(max(numbers))

for i in range(len(numbers)):
    if i > 0:
        first_positive_index = i
        break
for i in range(len(numbers), 0, -1):
    if i > 0:
        last_positive_index = i
        break
for i in range(first_positive_index, last_positive_index):
    sum_positive += numbers[i]
print('Между первым и последним положительными сумма', sum_positive)

for i in range(min_value, max_value):
    product_min_max *= numbers[i]
    if numbers[i] == 0:
        product_min_max = 0
print('Произведение между минимальным и максимальным ', product_min_max)

for i in range(len(numbers)):
    if numbers[i] < 0:
        sum_negative += numbers[i]
    if numbers[i] % 2 == 0:
        sum_even += numbers[i]
    if numbers[i] % 2 != 0:
        sum_odd += numbers[i]
    if numbers[i] % 3 == 0:
        product3 *= numbers[i]

print('Сумма отрицательных ', sum_negative)
print('Сумма чётных ', sum_even)
print('Сумма нечётных ', sum_odd)
print('Произведение кратных 3 ', product3)