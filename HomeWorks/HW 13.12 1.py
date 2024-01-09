# Задание 1
# Пользователь вводит с клавиатурыдва числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.


end1 = int(input('Введите начало диапазона > '))
end2 = int(input('Введите конец диапазона > '))


count_even = 0
sum_even = 0

count_odd = 0
sum_odd = 0

count_nine = 0
sum_nine = 0

for i in range(end1, end2 + 1):
    if i % 9 == 0:
        count_nine += 1
        sum_nine += i
    if i % 2 == 0:
        count_even += 1
        sum_even += i
    else:
        count_odd += 2
        sum_odd += i


print(f'Сумма чётных чисел {sum_even}, их среднее арифметическое {sum_even/count_even}')
print(f'Сумма нечётных чисел {sum_odd}, их среднее арифметическое {sum_odd/count_odd}')
print(f'Сумма чисел кратных 9 {sum_nine}, их среднее арифметическое {sum_nine/count_nine}')



# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %

length = int(input('Введите длину линии > '))
symbol = input('Введите символ для линии > ')

for i in range(0, length):
    print(symbol)




# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Numberis positive»,
# если меньше нуля «Numberis negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»


while True:
    num = int(input('Введите число > '))
    if num == 7:
        print('Good bye!')
        break
    if num > 0:
        print('Number is positive')
    elif num < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')





# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

sum = 0
min_num = 99999999
max_num = -99999999

while True:
    num = int(input('Введите число > '))
    if num == 7:
        print('Good bye!')
        break
    sum += num
    if num <= min_num:
        min_num = num
    if num >= max_num:
        max_num = num
    print(f'Сумма введённых чисел {sum}')
    print(f'Самое большое число {max_num}')
    print(f'Самое маленькое число {min_num}')