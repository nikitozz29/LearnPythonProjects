# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y

while True:
    num = int(input('Введите число > '))
    degree = int(input('Введите степень > '))
    print(f'Число {num} в степени {degree} равно {num ** degree}\n')




# Задание 2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

count = 0

for i in range(100, 1000):
    a = str(i)
    if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        # print(a)
        count += 1


print(count)




# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

count = 0

for i in range(100, 1000):
    a = str(i)
    if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        count += 0
    else:
        count += 1

for i in range(1000, 10000):
    a = str(i)
    if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
        count += 0
    else:
        count += 1

print(count)





# Задание 4
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.


while True:
    num = int(input('Введите число > '))
    a = str(num)
    res_str =''
    for i in a:
        if i != '3' and i != '6':
            res_str += i
    print(res_str)