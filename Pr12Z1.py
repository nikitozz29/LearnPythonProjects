# Задание 1
# Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
# на экран.

string = input('Введите строку > ')

new_string = string[: : -1]

print(new_string)