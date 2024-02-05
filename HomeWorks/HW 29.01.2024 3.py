# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра.Полученныйрезультат возвращаетсяизфункции.

def simple_count(num_list: list):
    result_count = 0
    for num in num_list:
        count = 0
        if num < 2:
            continue
        else:
            for i in range(2, num):
                if num % i == 0:
                    count += 1
        if count == 0:
            result_count += 1
    return result_count

num_list = [13, -4, 28, -9, 6, 3, 5]
print(simple_count(num_list))