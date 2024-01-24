def show_odd(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)
    
show_odd(1, 13)