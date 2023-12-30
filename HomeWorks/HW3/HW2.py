# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

sales1 = int(input('Введите продажи первого менеджера >'))
sales2 = int(input('Введите продажи второго менеджера >'))
sales3 = int(input('Введите продажи третьего менеджера >'))

sales = [sales1, sales2, sales3]


salarys = [0, 0, 0]

i = 0
for sale in sales:
    if sale <= 500:
        salarys[i] = 200 + sale * 1.03
    elif 500 < sale <= 1000:
        salarys[i] = 200 + sale * 1.05
    elif sale > 1000:
        salarys[i] = 200 + sale * 1.08
    i += 1


salarys[salarys.index(max(salarys))] += 200

# print(salarys)

i = 0
for salary in salarys:
    if salary == salarys[salarys.index(max(salarys))]:
        print(f'Менеджер {salarys.index(max(salarys)) + 1} лучший, он получает премию 200$, и его зарплата составляет {salarys[salarys.index(max(salarys))]}')
    else:
        print(f'Зарплата {i + 1} менеджера: {salarys[i]}')
    i += 1

