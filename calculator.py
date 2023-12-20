a = int(input('Введите первое чило\n>'))
print(a)
znak = input('Ведите действие с числами\n>')
print(str(a) + ' ' + znak)
b = int(input('Введите второе число\n>'))

def result(a, b, znak):
    if znak == '+':
        return a + b
    elif znak == '-':
        return a - b
    elif znak == '*':
        return a * b
    elif znak == '/':
        return a / b
    elif znak == '%':
        return a % b   

c = str(result) 
print(str(a) + ' ' + znak + ' ' + str(b) + ' = ' + c)
