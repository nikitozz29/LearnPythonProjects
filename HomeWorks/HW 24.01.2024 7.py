# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321—палиндром(первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.


import math


def check_palindrome(number):
    count = 0
    for i in str(number):
        count += 1
    number = str(number)
    if count % 2 == 0:
        num1 = number[: int(count / 2)]
        num2 = number[int(count / 2):]
        num3 = num2[::-1]
        if num1 == num3:
            return True
        else:
            return False
    else:
        num1 = number[:math.floor(count / 2)]
        num2 = number[math.ceil(count / 2):]
        if num1 == num2[::-1]:
            return True
        else:
            return False


print(check_palindrome(20203))
print(check_palindrome(20202))
print(check_palindrome(2003))
print(check_palindrome(2002))
print(check_palindrome(12))
print(check_palindrome(55))