# Задание 1
# Пользователь вводит число. Определить количество
# цифр в этом числе, посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
# Общение с пользователем организовать через меню.


while  True:

    num = int(input('Введите число > '))

    action = input('1.Определить количество цифр\n2.Посчитать сумму цифр\n3.Посчитать среднее арифметическое\n4.Определить количество нулей\n')

    if action == '1':
        count = 0
        str_num = str(num)
        for i in str_num:
            count += 1
        print(f'Количество цифр {count}')
    elif action == '2':
        sum = 0
        for i in str(num):
            sum += int(i)
        print(f'Сумма цифр {sum}')
    elif action == '3':
        count = 0
        sum = 0
        for i in str(num):
            count += 1
            sum += int(i)
        print(f'Среднее арифметическое {sum/count}')
    elif action == '4':
        count = 0
        for i in str(num):
            if i == '0':
                count += 1
        print(f'Количество нулей {count}')