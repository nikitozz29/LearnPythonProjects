number1 = int(input('Введите первое число > '))
number2 = int(input('Введите второе число > '))

action = input('Что нужно сделать?\n1)Найти сумму\n2)Найти разность\n3)Найти среднее арифметическое\n4)Найти произведение\n')

if action == 'Найти сумму' or '1' or '1)':
    print('Сумма ', number1 + number2)
elif action == 'Найти разность' or '2' or '2)':
    print('Разность ', number1 - number2)
elif action == 'Найти среднее арифметическое' or '3' or '3)':
    print('Среднее арифметическое ', (number1+number2)/2)
elif action == 'Найти произведение' or '4' or '4)':
    print('Произведение ', number1 * number2)
else:
    print('Проверьте ввод')

