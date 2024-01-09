# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

operation = input('Введите выражение\n>>> ')

if operation.__contains__('+'):
    operation = operation.split('+')
    print(int(operation[0]) + int(operation[1]))
if operation.__contains__('-'):
    operation = operation.split('-')
    print(int(operation[0]) - int(operation[1]))
if operation.__contains__('*'):
    operation = operation.split('*')
    print(int(operation[0]) * int(operation[1]))
if operation.__contains__('/'):
    operation = operation.split('/')
    print(int(operation[0]) / int(operation[1]))