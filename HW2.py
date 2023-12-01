salary = int(input('Какая у Вас зарплата? >'))
payment = int(input('Какой у Вас платёж по кредиту? >'))
debt = int(input('Какой у Вас платёж за услуги ЖКХ? >'))
result = salary-payment-debt

print(f'Ваш баланс {result} денег')
