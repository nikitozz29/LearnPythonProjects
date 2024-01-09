# Задание 2
# Написать программу, которая выводит на экран
# шахматную доску с заданным размером клеточки. Например, три,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

# size = int(input('Введите размер клетки > '))

# for i in range(0, 3):
#     for j in range(0, 4):
#         print('*' * size + '-' * size, end='')
#     print('')
# for i in range(0, 3):
#     for j in range(0, 4):
#         print('-' * size + '*' * size, end='')
#     print('')

size = int(input('Введите размер клетки > '))

for i in range(0, size):
    for j in range(0, 4):
        print('*' * size + '-' * size, end='')
    print('')
for i in range(0, size):
    for j in range(0, 4):
        print('-' * size + '*' * size, end='')
    print('')