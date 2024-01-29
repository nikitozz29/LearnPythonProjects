# Задание 2
# Есть список целых, заполненный случайными числами.
# На основании данных этого массива нужно:
# Создать список целых, содержащий только четные
# числа из первого списка;
# Создать список целых, содержащий только нечетные
# числа из первого списка;
# Создать список целых, содержащий только отрицательные числа из первого списка;
# Создать список целых, содержащий только положительные числа из первого списка.
# Практическое задание

import random

numbers = [random.randint(-100, 100) for i in range(40)]
print(numbers)

evens = []
odds = []
negatives = []
positives = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])
    if numbers[i] % 2 != 0:
        odds.append(numbers[i])
    if numbers[i] < 0:
        negatives.append(numbers[i])
    if numbers[i] >= 0:
        positives.append(numbers[i])

print(evens)
print(odds)
print(negatives)
print(positives)