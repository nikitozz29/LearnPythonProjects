# Задание 1
# Пользователь вводит число. Определить количество
# цифр в этом числе, посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
# Общение с пользователем организовать через меню.

while True:
    num = int(input('Введите число > '))
    print('Выберите номер\nМеню:')
    print('1. Определить количество цифр')
    print('2. Посчитать сумму цифр в числе')
    print('3. Посчитать среднее арифметическое цифр в числе')
    print('4. Определить количество нулей в числе')
    print('5. Выход')
    for i in range(0, 20):
        print('=', end='')
    

    action = input('\n>>>')

    sum = 0
    count = 0
    zero_counter = 0

    if action == '5':
        break
    elif action == '1':
        print(f'В числе {len(str(num))} цифр')
    elif action == '2':
        for i in str(num):
            sum += int(i)
        print(f'Сумма цифр {sum}')
    elif action == '3':
        for i in str(num):
            sum += int(i)
            count += 1
        print(f'Среднее арифметическое цифр в числе {sum/count}')
    elif action == '4':
        for i in str(num):
            if i == '0':
                zero_counter += 1
        print(f'Количество нулей в числе {zero_counter}')
