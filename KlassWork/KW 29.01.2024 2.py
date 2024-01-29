# Задание 2
# Напишите функцию для нахождения максимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

import random
from random import randint


number = []
for i in range(0, 10):
    number.append(random.randint(1, 100))

def max_in_list(number: list):    
    return max(number)
    
print(max_in_list(number))