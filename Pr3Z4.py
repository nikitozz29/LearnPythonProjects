# ; Задание 4
# ; Пользователь вводит с клавиатуры температуру по
# ; шкале Цельсия. Требуется перевести температуру в градусы по Фаренгейту и вывести на экран.

Celsium = input('Температура по Цельсию > ')
Farenheit = float(Celsium) * 1.8 + 32

print('Температура по Фаренгейту > ', str(Farenheit))

