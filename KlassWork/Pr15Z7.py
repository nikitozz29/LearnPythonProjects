def happy(num):
    num = str(num)
    num1 = num[0 : 3]
    num2 = num[3 : 6]
    sum1 = 0
    sum2 = 0
    for i in num1:
        sum1 += int(i)
    for i in num2:
        sum2 += int(i)
    if sum1 == sum2:
        return True
    else:
        return False
    
print(happy(123123))
print(happy(123456))