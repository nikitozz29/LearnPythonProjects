# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.


def show_evens(num1, num2):
    evens = []
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            evens.append(i)
    for i in evens:
        print(i, end=' ')


show_evens(-6, 12)
print('\n\n')
