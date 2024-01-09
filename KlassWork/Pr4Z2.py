number = int(input('Проверим число на чётность. Введите число > '))

if number == 0:
    print('Введите не ноль')
elif number % 7 == 0:
    print(number, 'Число кратно 7')
else:
    print(number,  ' Число не кратно 7')