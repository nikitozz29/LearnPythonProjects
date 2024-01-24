def easy(num):
    count_degree = 0
    for i in range(2, num):
        if num % i == 0:
            count_degree += 1
    if count_degree == 0:
        return True
    else:
        return False

print(easy(3))
print(easy(4))
print(easy(5))