#in direction write horizontal or vertical
def symbol_line(lenght, direction, symbol):
    if direction.lower() == 'horizontal':
        for i in range(0, lenght):
            print(symbol, end='')
    elif direction.lower() == 'vertical':
        for i in range(0, lenght):
            print(symbol)

symbol_line(10, 'horizontal', '*')
symbol_line(10, 'vertical', '*')