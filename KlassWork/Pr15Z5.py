def sum_numbers(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
    return sum

print(sum_numbers(-5, 3))