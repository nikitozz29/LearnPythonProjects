# Задание 4
# Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
# основания треугольника и размер высоты.

height = int(input('Введите высоту треугольника > '))
base = int(input('Введите основание треугольника > '))

area = height * base / 2

print('Площадь треугольника: ', area)
