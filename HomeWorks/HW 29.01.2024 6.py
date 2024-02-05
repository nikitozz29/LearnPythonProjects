# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержащий полученные результаты.

def exponentiation(num_list: list, number):
    new_list = []
    for num in num_list:
        new_list.append(num ** number)
    return new_list

num_list = [13, -4, 28, -9, 6, 3, 5, 13]

print(exponentiation(num_list, 2))