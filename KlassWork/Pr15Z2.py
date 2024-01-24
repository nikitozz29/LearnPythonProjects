def show_odd(num1, num2):
    odds = []
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            odds.append(i)
    for i in odds:
        print(i, end=' ')
    
show_odd(1, 13)