# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.

def multiplication(num_list: list):
    result = 1
    for number in num_list:
        result *= number
    return result

num_list = [13, -4, 28, -9, 6, 3]
print(multiplication(num_list))