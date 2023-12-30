largestNumber = -99999999
counter = 0
number = int(input("Введите число и напишите -1 для завершения программы: "))
while number != -1:
    if number == -1:
      continue
    counter += 1
    if number > largestNumber:
      largestNumber = number
    number = int(input("Введите число и напишите -1 для завершения программы: "))
if counter:
 print("Наиболшее число", largestNumber)
else:
 print("Вы не ввели число.")