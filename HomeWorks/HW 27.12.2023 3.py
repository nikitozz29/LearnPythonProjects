# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# Сформировать третий список, содержащий элементы
# обоих списков;
# Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# Сформировать третий список, содержащий элементы
# общие для двух списков;
# Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

import random

digits1 = [random.randint(-100, 100) for i in range(50)]
digits2 = [random.randint(-100, 100) for i in range(50)]

new_list1 = digits1 + digits2
new_list2 = list(set(new_list1))
new_list3 = list(set(digits1).intersection(set(digits2)))
new_list4 = list(set(digits1)) + list(set(digits2))
new_list5 = [min(digits1), min(digits2), max(digits1), max(digits2)]

print(digits1)
print(digits2)

print(new_list1)
print(new_list2)
print(new_list3)
print(new_list4)
print(new_list5)
