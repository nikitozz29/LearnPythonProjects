# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

def num_del(num_list: list, number):
    count = 0
    for num in num_list:
        if num == number:
            num_list.remove(num)
            count += 1
    return count

num_list = [13, -4, 28, -9, 6, 3, 5, 13]

print(num_del(num_list, 13))