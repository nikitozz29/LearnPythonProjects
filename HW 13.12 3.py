# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Numberis positive»,
# если меньше нуля «Numberis negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»


while True:
    num = int(input('Введите число > '))
    if num == 7:
        print('Good bye!')
        break
    if num > 0:
        print('Number is positive')
    elif num < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')

