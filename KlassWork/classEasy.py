# class Student:
#     def __init__(self, name, age, average_grade):
#         self.__name = name
#         self.__age = age
#         self.__average_grade = average_grade

#     def get_name(self):
#         return self.__name
#     def set_name(self, n):
#         self.__name = n

#     def get_age(self):
#         return self.__age
#     def set_age(self, a):
#         self.__age = a

#     def get_average_grade(self):
#         return self.__average_grade
#     def set_average_grade(self, g):
#         self.__average_grade = g

#     def print(self):
#         print(f'Student {self.get_name()} {self.get_age()} years old, average grade - {self.get_average_grade()}')

# student = Student('иван', 2, 2)

# student.set_name('Nikita')
# student.set_age(28)
# student.set_average_grade(12)

# student.print()



# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


#     def print(self):
#         print(f'Book {self.title} of author {self.author} published {self.year}')

# my_book = Book('Dune', 'Frank Herbert', 1965)

# my_book.print()


# class Calculator:
#     def __init__(self, expr: str):
#         self.expr = expr
#         new_str = ''
#         if expr.__contains__('+'):
#             new_str = expr.split('+')
#             print(float(new_str[0]), '+', float(new_str[1]), '=', float(new_str[0]) + float(new_str[1]))
#         elif expr.__contains__('-'):
#             new_str = expr.split('-')
#             print(float(new_str[0]) - float(new_str[1]))
#         elif expr.__contains__('*'):
#             new_str = expr.split('*')
#             print(float(new_str[0]) * float(new_str[1]))
#         elif expr.__contains__('/'):
#             new_str = expr.split('/')
#             print(float(new_str[0]) / float(new_str[1]))

    
    
# addition = Calculator('2+3')
# subtraction = Calculator('13-9')
# multiply = Calculator('2*8')
# divide = Calculator('27/3')

# class Auto:
#     def __init__(self, mark, model, year: int):
#         self.mark = mark
#         self.model = model
#         self.year = year

#     def age_auto(self):
#         year = int(input('В каком вы году находитесь? >> '))
#         print(f'Возраст автомобиля {year - self.year}  лет')

# car = Auto('Dodge', 'Stratus 2', 2001)
# car.age_auto()

# class AreaCalculator:
#     calculations_counter = 0

#     @staticmethod
#     def calculate_triangle_area(base, height):
#         AreaCalculator.calculations_counter += 1
#         return 0.5 * base * height
    
#     @staticmethod
#     def calculate_rectnagle_area(length, width):
#         AreaCalculator.calculations_counter += 1
#         return length * width
    
#     @staticmethod
#     def calculate_square_area(side):
#         AreaCalculator.calculations_counter += 1
#         return side * side
    
#     @staticmethod
#     def calculate_rhombus_area(diag1, diag2):
#         AreaCalculator.calculations_counter += 1
#         return (diag1 * diag2)/2
    
# print(AreaCalculator.calculate_rectnagle_area(3, 5))

# class StrangeCalculator:

#     @staticmethod
#     def max_num(num1, num2, num3, num4):
#         return max(num1, num2, num3, num4)
    
#     @staticmethod
#     def min_num(num1, num2, num3, num4):
#         return min(num1, num2, num3, num4)
    
#     @staticmethod
#     def average(num1, num2, num3, num4):
#         return (num1 + num2 + num3 + num4)/4
    
#     @staticmethod
#     def factorial(num):
#         fact = 1
#         for i in range(1, num + 1):
#             fact *= i
#         return fact
    
# print(StrangeCalculator.max_num(-3, 0, 2, 10))
# print(StrangeCalculator.min_num(-3, 0, 2, 10))
# print(StrangeCalculator.average(-3, 0, 2, 10))
# print(StrangeCalculator.factorial(10))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Builder(Human):
    def __init__(self, name, age, construction_experience):
        Human.__init__(self, name, age)
        self.constrction_experience = construction_experience

    def build_house(self):
        print(f'{self.name} is building a house.')

class Sailor(Human):
    def __init__(self, name, age, sailing_experience):
        Human.__init__(self, name, age)
        self.sailing_experience = sailing_experience
    def song(self):
        print('What will we do with a drunken sailor?\nWhat will we do with a drunken sailor?\nWhat will we do with a drunken sailor?\nEarly in the morning!')

class Pilot(Human):
    def __init__(self, name, age, flying_experience):
        Human.__init__(self, name, age)
        self.flying_experience = flying_experience
    def fly_plane(self):
        print(f'{self.name} is flying a plane')

builder = Builder('John', 30, 5)
builder.build_house()

sailor = Sailor('Morgan', 28, 15)
sailor.song()

pilot = Pilot('Gagarin', 52, 25)
pilot.fly_plane()