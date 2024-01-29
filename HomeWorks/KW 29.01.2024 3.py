# Задание 3
# Напишите функцию, определяющую количество повторяющихся чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

import random
from random import randint


number = [1, 2, 3, 3, 2, 4, 5 ,6, 22, 23]
# for i in range(0, 10):
#     number.append(random.randint(1, 10))

def repeat_in_list(number: list):   
    count = 0 
    for i in number:
        if number.count(i) > 1:
            del number[i]
            count += 1
    return count

    
print(repeat_in_list(number))