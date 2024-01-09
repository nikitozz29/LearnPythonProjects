# Задание 3
# Пользователь с клавиатуры вводит элементы списка
# целых. Необходимо посчитать сумму всех элементов
# и их среднеарифметическое. Результаты вывести на
# экран.

numbers = input('Введите целые числа через пробел >> ')

list_numbers = numbers.split()

for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i])

print(f'Сумма чисел: {sum(list_numbers)}, среднее арифметическое: {sum(list_numbers)/len(list_numbers)}')