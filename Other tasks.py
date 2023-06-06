# import requests
# import bs4
#
# import numpy as np
# a = np.

# i = 0
# while i < 11:
#     print(i)
#     i = i +1

# a = 8
# b = 1
# while(a>5):
#     a-=2
#     b+=a
#     print (b)

# a =1
# b = 3
# while(a!=5):
#     a+=1
#     b+=a
#     print(b)

# num = int(input('INput any number, please'))
# data = []
# while num!=0:
#     data.append(num)
#     num = int(input())
# data.sort()
# print(data)

# input('Введите любое количестов слов через ентер')
# words = input()
# data = []
# while words !='':
#     if words not in data:
#         data.append(words)
#     words = input()
# for item in data:
#     print(item)

# num = int(input())
# if num%2==0:
#     print('чётное число',num)
# else:
#     print('нечетное число',num)
#
# letter = input('input a text')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('гласная буква', letter)
# elif letter == 'y':
#     print('согласная и гласная')
# else:
#     print('Согласная', letter)

# mas = [1,2,2,4,5,]
# for item in mas:
#      print(item, end=', ')

# meel = ['мясо', 'сыр', 'сгущенка', 'конфеты']
# for food in meel:
#     if food == 'сгущенка':
#         print('no sugar!', food)
#         break
#     print('отлично перекусил', food)
# else:
#     print('хорошо, что без сгущенки')
#
# print('Good meel')


# meel = ['мясо', 'сыр', 'сгущенка', 'конфеты']
# for food in meel:
#     if food == 'сгущенка':
#         print('no sugar!', food)
#         continue
#     print('отлично перекусил', food)
# else:
#     print('хорошо, что без сгущенки')
#
# print('Good meel')

    # print('''a lot
    # of ''
    # strings''')

    # text = 'Длиннная строка'
    # print('первый знак ''')

# a = 1
# b = 73
# c = -12
# d = 2
#
#
# e=a+b
# print(e,',',type(e))

# a = -13
# b = 7
#
# a = a - b
# b = a + b
# a = b - a
#
# print(a,
#       b)

# print(3 > 10)
#
# print(2**23)
# print(50/3)

# a = -5
# b = 2
# q = a // b
# print('результатделения -5 на 2','\n',q,'\nостаток от деления = ',a%b)
# print('\nСледующее выражение')
# a = -6
# b = 2
# q = a // b
# print('результатделения -6 на 2','\n',q,'\nостаток от деления = ',a%b)
#
# f = 653457
# g = 123493
# print(f**g)
#
# 11*2.5/3
# a=11
# b=2.5
# c=3
# print(round(a*b/c,2))
#
# print(11*2.5/3)
#
# pi=3.14159
# print(round(pi**2/2))

# s = 'Hello!'
# print(s[-3:-1])
# print(s[-1])
#
# numbers = '1 2 3 4 5 6 7'
# numbers_splitSTR = numbers.split(' ')
# numbers_columnLines = '\n'.join(numbers_splitSTR)
# print('Output order:','\v',numbers_columnLines)
#
# # numb = float(input('введите число '))
# # print(numb,',',type(numb))
#
# pi = 31.4159265
# print ("%.4e" % (pi))

# day = 14
# month = 12
# year = 2012
#
# print("%d.%d.%d" % (day, month, year))
#
# L = ["а", "б", "в", 1, 2, 3, 4]
#
# print(L[3::-1])
# print(L[:3:-1])
# # [1, "в", "б", "а"]
# # [4, 3, 2]
#
# L = ['3.3', '4.4', '5.5', '6.6']
#
# print (list (map (float, L)))
#
# string = input('введите неколько целых чисел через пробел: \n')
# print(string)
# list_of_string = string.split()
# print(string, type(string))
# list_of_numbers = list(map(int, list_of_string))
# print(list_of_numbers,type(list_of_numbers))
# print(sum(list_of_numbers[::3]))

# Первое и последнее числа последовательности должны поменяться местами.
# В конец списка нужно добавить сумму всех чисел.

# str_numbers = input('Input some numbers with spaces ')
# temp_list_of_num = str_numbers.split()
# list_of_num = list(map(int, temp_list_of_num))
# list_of_num[0], list_of_num[-1] = list_of_num[-1], list_of_num[0]
# list_of_num.append(sum(list_of_num))
# print(list_of_num)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))

# Напишите программу, которая получает на вход название книги - title,
# фамилию автора - author и год выпуска - year.
#
# Полученные данные должны быть преобразованы в словарь book с ключами:
# title, author, year. Причем year нужно преобразовать в тип int.
#
# Примечание. Обратите внимание, что для отправки кода на проверку переменные title, author, year объявлять не нужно.
# Не забудьте удалить строку кода с её объявлением перед тем, как отправить код на тестирование.

# title = input('Введите название книги: ')
# author = input('Введите фамилию автора книги: ')
# year = int(input('Введите год выпуска книги: '))
#
# book = {'title':title,'author':author, 'year': year}
# print(book, type(book['year']),type(['author']))
#
# a={'a', 'b', 'c', 'd'}
# print(a)
#
#
# L = [1,1,2,3,2]
#
#
# c_L = list(set(L))
# print(c_L)


# text = ".."
# L_text = list(set(text))
# print(L_text, '\n',len(L_text))
# print(L_text, type(L_text))
# print(type(L_text))

# a = [1,2,3,4,5,6,7,8]
# b = [2,4,6,8,10,12]
#
# LS1, LS2 = set(a), set(b)
# print(LS1, '-', 'type of var.L_1:', type(LS1))
#
# print(LS2, '-', 'type of var.L_2:', type(LS2))
#
# dif_LS1_LS2 = LS1.symmetric_difference(LS2)
# print(dif_LS1_LS2)

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# c = id(a)-id(b)
# print(c)


# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# x=int(input('Numbers'))
# if x is not int:
#     print(x)
# else:
#     print(x)

# L = [0,4,4,3,]
# if L:
#     print('Список - ', L)
# else:
#     print('Список пустой')

'''Запишите условие, которое является истинным,
когда только одно из чисел А, В и С меньше 45.
Иногда проще записать все условия и не пытаться упростить их.'''

# a,b,c = int(input("Введите любое целое число (a): ")), \
#     int(input("Введите любое целое число (b): ")), \
#     int(input("Введите любое целое число (c): "))
#
# if ((a>45) and (b>45) and (c<45)) or\
#    ((a<45) and (b>45) and (c>45)) or \
#    ((a>45) and (b<45) and (c>45)):
#
#    print('Есть число меньше 45')
# else:
#     print('Введите числа ещё раз: либо нет меньше 45, либо их больше одного')

# Как вытащить именно то число, чтобы отобразилосьв  программе?

'''Запишите логическое выражение, которое определяет, 
что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.'''

# a = int(input("put a number for 'a': "))
# if (-10<=a<=-1) or (2<=a<=15):
#     print('Число в запретных интервалах. Потворите ввод')
# else:
#     print(a)
#  # это получилось условие. Теперь пробуем логически.
#
# a = int(input("put a number for 'a': "))
# if not ((-10<=a<=-1) or (2<=a<=15)):
#     print('число, где надо. ', a)
# else:
#     print('Число в запретных промежутках. ', a)

'''Дано двузначное число. Определите, входит ли в него цифра 5. 
Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.'''

# N = int(input('Введите двузначное число: '))
# if N % 5 == 0:
#     print('Bingo! ', N)
#
# else:
#     print(N, 'Repeat')
# New_N = str(N)
# if '5' in New_N:
#     print(New_N)
# else:
#     print('error')

# if 5 in N_L:
#     print(N_L)
# else:
#     print(not N_L)

# N = int(input('Input any numb.^ '))
# frst_dig = N // 10
# scnd_dig = N % 10
#
# print(frst_dig, scnd_dig)
# print((frst_dig == 5) or (scnd_dig == 5))

'''Проверьте, все ли элементы в списке являются уникальными.
Можно попроювать через множества.'''
# a_lot_of = [1,23,45,6,7,3,2,2,2,54,90]
# check_a_lot_of = set(a_lot_of)
# print(check_a_lot_of, type(check_a_lot_of))
#
# if len(a_lot_of) == len(check_a_lot_of):
#     print('Equal')
# else:
#     print('not equal')
# '\n'
# '''или так'''
# new_L = [1,2,3,4,4,5,6,5,6,]
# print(len(new_L)==len(set(new_L)))

'''Дано натуральное восьмизначное число. 
Выясните, является ли оно палиндромом 
(читается одинаково слева направо и справа налево).'''

# thing = int(input('type a num: '))
# print(thing)
# print(str(thing) == str(thing)[::-1])

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# n = 6
# while True:
#     if n % 3 == 0:
#         n = n // 3
#         n += 1
#         if n == 1:
#             break
#         print('Последнее число: ', n)
#     else:
#         break
#     print('Итоговое последнее число: ', n)
#
# n = int(input('Put a num here: '))


# if n % 2 != 0:

# def check_h(n):
#     while n>1:
#         if n % 2 == 0:
#             n /= 2
#             if n == 1:
#                 return True
#                 print('Yahoo 2')
#         print("Yahoo!", n)
#     return False


# L = [1,5,7,3,9,-4,23,6,0]
# it = []
# for i in L:
#     if i % 2 == 0:
#         it.append(i)
# print(f'Все чётные числа в списке - {it}')
# print(f'Максимально значение из списка среди чётных - {max(it)}')


'''Сумма чисел, кратных числу "6"'''

# number = int(input('Type a number: '))
# sum = 0
#
# while number != 0:
#     if number % 6 == 0:
#         sum += number
#     elif number % 6 != 0:
#         print('Вы ввели число не кратное числу "6"')
#     number = int(input('Type a number again: '))
#
# print(f'Сумма чисел, кратных числу "6" - {sum}')

'''Количество чисел, кратных числу "4"'''

# number = int(input('Type a number: '))
# sum = 0
# count = 0
# while number != 0 and count < 4:
#     if number % 4 == 0:
#         sum += number
#         count += 1
#     elif number % 4 != 0:
#         print('Вы ввели число не кратное числу "4"')
#     number = int(input('Type a number again: '))
#
# print(f'Сумма чисел, кратных числу "4" - {sum};'
#       ,f'\nколичество чисел, кратных числу "4" - {count}.')


'''Из последовательности натуральных чисел,
количество чисел не более 1000, размер числа не больше 30 000'''

# number = int(input('Type a number: '))
# # L_numbers = []
# # sum = 0
# count = 0
# i_4 = 30000
# while number != 0: # and count < 10 and number < 30000:
#     # L_numbers.append((number))
#     # sum += number
#     # count += 1
#     if number % 10 == 4 and number < i_4:
#         i_4 = number
#     number = int(input('Type a number again: '))
# print(i_4)

# print(L_numbers)
# print(f'Сумма чисел, кратных числу "4" - {sum};'
#       ,f'\nколичество чисел, кратных числу "4" - {count}.')

# n = int(input('Введите число: '))
# while True:
#     if n % 3 == 0:
#         n = n // 3
#
#     #     if n == 1:
#     #         break
#     # n += 1
#     # # else:
#     # #     break
#     print('Итоговое последнее число: ', n)

    # L = [2,3,-1,5,6]
    # # print(L)
    # L = list(map(int, input('input: ').split()))
    # print(not any(L))
    # # # print(all(L_1),type(all(L_1)))
    # #
    # # N = list(map(int, input().split()))
    # # N = print()
    # i = 2
    # j = 2
    # M = [[i*j for j in range(1,11)] for i in range(1,11)]
    # for i in M:
    #     print(i, end='\n')

    # T = [[i*j for j in range(1,11)] for i in range(1,11)]
    # for i in T:
    #     print(i,end=",\n")

    # a = 3
    # if a % 2 == 0:
    #     print(bool(a))
    # else:
    #     print(not a)

    # k = []
    # for i in range(0,6):
    #     if i % 2 == 0:
    #         k.append(bool(i))
    #     else:
    #         k.append(not i)
    # print(k)

    # L = []
    #
    # for a in some_iter_obj:
    #     if cond:
    #         L.append(a)

    # L = [int(input()) % 2 == 0 for a in range(5)]
    # # L = [bool(int(input())) for i in range(5)]
    # print(any(L) and not all(L))
    # L = [i for i in range(10)]
    # print(L)
    # M = [i for i in range(10, 0, -1)]
    # print(M)
    # N = [L[i] * M[i] for i in range(10)]
    # # for i in range (10):
    # #     N.append(L[i] * M[i])
    # print(N)
    # # for a,b in zip(M,L):
    # #     print('a = ',a,', b = ', b, ', c = ')
    # Z = [a + b for a, b in zip(L, M)]
#
# from matplotlib import pyplot as plt
# import numpy as np
#
# # Generate 100 random data points along 3 dimensions
# x, y, scale = np.random.randn(3, 100)
# fig, ax = plt.subplots()
#
# # Map each onto a scatterplot we'll create with Matplotlib
# ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
# ax.set(title="Some random data, created with JupyterLab!")
# plt.show()

class Person:
    def __init__(self, name='', id_numb=0, birth_date='', **kwargs):
        self.name = name
        self.id_numb = id_numb
        self.birth_date = birth_date
    def get_info(self):
        print('Данные экземпляра:', self.name, '\n',
              self.id_numb, '\n',
              self.birth_date)
    def is_Employee(self):
        return False

class Empl_1(Person):
    def __init__(self, name, id_numb, birth_date='', departm='', salary=0, **kwargs):
        self.departm = departm
        self.salary = salary
        Person.__init__(self, name, id_numb, birth_date, **kwargs)
    def is_Employee(self):
        return True
#     def employee_info(self):
#         print('Данные экземпляра:',self.name, '\n',
#              self.idNum)

pers_1 = Person(name='Kit', id_numb=1234, birth_date='12.06.77')

pers_2 = Person(name='Joel', id_numb=1001, birth_date='13.05.66')
emp = Empl_1(name='Number_two', id_numb=1002, departm='security', salary=30000)

pers_2.get_info()
emp.get_info()


'''try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!")
#
try:
    x = int(input('введите число/числа - '))
    print(x)
except ValueError as error:
    print(error)
    print('Введите число заново')
else:
    print(f'Вы ввели правильное число - {x}')
finally:
    print('Выход из программы')'''


class NonPositiveDigitException(ValueError):
    pass
class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')
