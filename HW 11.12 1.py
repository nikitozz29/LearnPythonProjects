# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.

num1 = int(input('Введите начало диапазона >'))
num2 = int(input('Введите конец диапазона >'))

for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i)