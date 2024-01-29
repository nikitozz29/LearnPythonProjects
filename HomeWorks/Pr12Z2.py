# Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
# количества на экран.

string = input('Введите строку >> ')

count_letters = 0
count_digits = 0

for i in string:
    if i.isalpha():
        count_letters += 1
    elif i.isdigit():
        count_digits += 1

print(f'В строке букв: {count_letters}, и цифр:  {count_digits}.')

