# Напишите функцию, которая преобразует введённое пользователем число
# в бинарное представление и подсчитывает количество единиц в числе


def from_digit_to_bin():
    digit = int(input('Введите число  > '))
    count = 0
    bin_digit = bin(digit)
    for i in bin_digit:
        if i == '1':
            count += 1
    print(bin_digit + ', ', count)


if __name__ == '__main__':
    while True:
        from_digit_to_bin()
