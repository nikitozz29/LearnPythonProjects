def checkio(array: list[int]) -> int:
    # your code here
    print(array.index(84))
    sum_array = 0
    if not array:
        return 0
    else:
        for i in array:
            if array.index(i) % 2 == 0:
                sum_array += i
        return sum_array * array.pop()


print(checkio([-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62, 26, -76, 55, -24, 84, 49, -65, 41]))
