# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

count = 0

for i in range(100, 1000):
    a = str(i)
    if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        count += 0
    else:
        count += 1

for i in range(1000, 10000):
    a = str(i)
    if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
        count += 0
    else:
        count += 1

print(count)