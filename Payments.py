# Дан массив покупок
# payments = [10, 65, 89, 65, 65, 89, 55, 64, 82, 10, 10, 10, 10, 89, 10]
# Каждая третья покупка товара с одинаковой ценой бесплатная, нужно посчитать итоговую сумму







def sum_payments(payments):
    for pay in payments:
        if payments.count(pay) % 3 == 0 or payments.count(pay) % 3 > 1:
            for i in range(0, payments.count(pay) // 3):
                payments.remove(pay)
    print(sum(payments))

if __name__ == '__main__':
    payments = [10, 65, 89, 65, 65, 89, 55, 64, 82, 10, 10, 10, 10, 89, 10]
    sum_payments(payments)
