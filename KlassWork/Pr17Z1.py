# Задание 1
# Написать рекурсивную функцию нахождения степени 
# числа.

def recursive(num, deg):
    num *= num
    print(num)
    if deg == 0:
        return
    else:
        recursive(num, deg - 1)

recursive(2, 5)