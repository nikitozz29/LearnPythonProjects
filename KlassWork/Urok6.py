import math

# x=float(input('Enter x: '))
# y = math.sqrt(x)

# print('The square root of', x, 'equals to', y)


# firstNumber = int(input('Enter the first number: '))
# secondNumber = int(input('Enter the second number: '))

# # if secondNumber != 0:
# #     print(firstNumber / secondNumber)
# # else:
# #     print('This operation cannot be done.')

# # print('THE END.')

# try:
#     print(firstNumber / secondNumber)
# except:
#     print('This operation cannot be done.')

# print('THE END.')


# try:
#     print('1')
#     x = 1 / 0
#     print('2')
# except:
#     print('Oh dear, something went wrong...')


# print('3')

#
#     try:
#         x = int(input('Enter a number: '))        
#         y = 1 / x
#         print (y)
#     except ZeroDivisionError:
#         print('You cannot divide by zero, sorry.')
#     except ValueError:
#         print('You must enter an integer value.')
#     except:
#         print('Oh dear, something went wrong...')


try:
    y = 1 / 0
except ZeroDivisionError:
    print('Zero Division!')
except ArithmeticError:
    print('Arithmetic Error')

print('THE END')