import math

diametr = int(input('Введите диаметр окружности > '))


action = input('Вы хотите узнать:\n1.Периметр\n2.Площадь\n')

if action.lower() == '1' or 'периметр':
    print(f'Диаметр круга {math.pi * diametr}')
elif action.lower() == '2' or 'площадь':
    print(f'Площадь круга {math.pi * ((diametr/2)**2)}')

