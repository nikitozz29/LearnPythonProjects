# Задание 1
# Напишите функцию, вычисляющую сумму
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.

import random
from random import randint


number = []
for i in range(0, 10):
    number.append(random.randint(1, 100))

def sum_list(number: list):    
    return sum(number)
    
print(sum_list(number))
