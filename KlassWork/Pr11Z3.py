# Задание 3
# Написать программу, которая проверяет пользователя
# на знание таблицы умножения. Программа выводит на
# экран два числа, пользователь должен ввести их произведение. Разработать несколько уровней сложности (от
# личаются сложностью и количеством вопросов). Вывести
# пользователю оценку его знаний.                                                                                        

import random

while True:
    print('1. Лёгкий уровень')
    print('2. Средний уровень')
    print('3. Сложный уровень')
    print('4. Выход')

    choice = input('>>> ')

    if choice == '4':
        break
    elif choice == '1':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        
        action = int(input(f'Введите произведение {num1} и {num2}\n>>> '))

        while action != num1*num2:
            action = int(input('Попробуй ещё >>> '))
        print('Верно!')
        continue        
    elif choice == '2':
        num1 = random.randint(1, 11)
        num2 = random.randint(1, 11)
        
        action = int(input(f'Введите произведение {num1} и {num2}\n>>> '))

        while action != num1*num2:
            action = int(input('Попробуй ещё >>> '))
        print('Верно!')
        continue        
    elif choice == '3':
        num1 = random.randint(1, 21)
        num2 = random.randint(1, 21)
        
        action = int(input(f'Введите произведение {num1} и {num2}\n>>> '))

        while action != num1*num2:
            action = int(input('Попробуй ещё >>> '))
        print('Верно!')
        continue        
    print('Верно!')