number1 = int(input('Введите первое число > '))
number2 = int(input('Введите второе число > '))

if number1 > number2:
    print(f'{number1} больше {number2}')
elif number2 > number1:
    print(f'{number2} больше {number1}')
else:
    print('Числа равны')

print('Наибольшее число ', max(number1, number2))
