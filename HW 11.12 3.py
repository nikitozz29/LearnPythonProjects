# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывеДомашнее задание
# 1
# сти слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.

num1 = int(input('Введите начало диапазона >'))
num2 = int(input('Введите конец диапазона >'))

for i in range(num1, num2 + 1):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    else:
        print(i)