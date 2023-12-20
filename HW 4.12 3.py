# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

meters = float(input('Введите количество метров >'))

action = input('Перевести в \n1.Мили\n2.Дюймы\n3.Ярды\n>>')

if action.lower() == '1' or action.lower() == 'мили':
    print(f'В {meters} метрах {meters * 0.000621} миль')
elif action == '2' or action.lower() == 'дюймы':
    print(f'В {meters} м {meters * 39.37} дюймов')
elif action == '3' or action.lower() == 'ярды':
    print(f'В {meters} м {meters * 1.093613} ярдов')
else:
    print('Проверьте ввод')
