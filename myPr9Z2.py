# Задание 2
# Написать программу – конвертер валют. Реализовать
# общение с пользователем через меню

print('Добро пожаловать в конвертер валют!\nЧтобы выйти напишите "0" или "выход"')
n = True
while n:
    cash = input('Сколько валюты на руках? > ')
    if cash == '0' or cash == 'выход':
        print('Пока!')
        n=False
        break
    choice1 = input('Итак, вы можете перевести:\n1.Рубли\n2.Доллары\n3.Евро\n')
    if choice1 == '0' or choice1.lower() == 'выход':
        print('Пока!')
        n=False

    if choice1 == '1' or choice1.lower() == 'рубли':
        choice2 = input('Во что переводим?\n1.Доллары\n2.Евро\n')
        
        if choice2 == '1' or choice2.lower() == 'доллары':
            print(f'{cash} деревянных - это {90 * float(cash)} долларов')
        elif choice2 == '2' or choice2.lower() == 'евро':
            print(f'{cash} деревянных - это {100 * float(cash)} евро')
        elif choice2 == '0' or choice2.lower() == 'выход':
            print('Пока!')
            n=False

    if choice1 == '2' or choice1.lower() == 'доллары':
        choice2 = input('Во что переводим?\n1.Рубли\n2.Евро\n')
        
        if choice2 == '1' or choice2.lower() == 'рубли':
            print(f'{cash} бакинских - это {float(cash)/90} рублей')
        elif choice2 == '2' or choice2.lower() == 'евро':
            print(f'{cash} бакинских - это {float(cash) * 0.9} евро')
        elif choice2 == '0' or choice2.lower() == 'выход':
            print('Пока!')
            n=False

    if choice1 == '3' or choice1.lower() == 'евро':
        choice2 = input('Во что переводим?\n1.Доллары\n2.Рубли\n')
        
        if choice2 == '1' or choice2.lower() == 'доллары':
            print(f'{cash} евро - это {1.08 * float(cash)} долларов')
        elif choice2 == '2' or choice2.lower() == 'рубли':
            print(f'{cash} евро - это {float(cash)/100} рублей')
        elif choice2 == '0' or choice2.lower() == 'выход':
            print('Пока!')
            n=False
    print('Продолжаем конвертировать!')
    