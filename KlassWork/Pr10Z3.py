# Задание 3
# Пользователь вводит с клавиатуры размер стороны
# квадрата. Требуется отобразить на экран незаполнен
# ный квадрат (отображаются только границы квадрата).
# Размер стороны равен введённому размеру

box = int(input('Введите длину стороны квадрата > '))

# print('*' * box)
#
# for i in range(0, box - 2):
#     print('*' + ' ' * (box - 2) + '*')
#
# print('*' * box)


for i in range(0, box):
    if i == 0 or i == box - 1:
        print('*' * box)
    else:
        print('*' + ' ' * (box - 2) + '*')