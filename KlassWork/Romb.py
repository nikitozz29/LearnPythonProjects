size = int(input('Введите сторону ромба > '))

for i in range(0, size):
    for j in range(1, size + 1):
        print(' ' * (size - j), end='')
        if j == 1:
            print('*')
        elif j % 2 != 0:
            print('*' * (j+2), end='')
            print('')
        else:
            print('*' * (j + 1), end='')
            print('')

