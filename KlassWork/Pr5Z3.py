cost = int(input('Сколько стоит приставка? > '))
quntity = int(input('Сколько приставок? > '))
discount = float(input('Введите процент скидки > '))

action = input('Вы хотите узнать стоимость: \n1.Всего заказа\n2.Одной приставки\n')


if action.lower() == '1' or 'всего заказа':
    print(f'Стоимость заказа {(cost - cost * (discount/100)) * quntity}')
elif action.lower() == '2' or 'одной приствки':
    print(f'стоимость приставки {cost - cost * (discount/100)}')
