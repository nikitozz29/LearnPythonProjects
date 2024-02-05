# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

def fusion(first_list: list, second_list: list):
    third_list = first_list + second_list
    return third_list

first_list = [13, -4, 28, -9, 6, 3, 5, 13]
second_list = [13, -4, 28, -9, 6, 3, 5, 13]

print(fusion(first_list, second_list))