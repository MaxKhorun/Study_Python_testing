# x = int(input('Введите год - '))
# def is_leap_year(x):
#     return (x%400==0) or ((x%4==0) and (x%100!=0))
# print(is_leap_year(x))
#
'''Определяем четные и нечетные числа'''
# A = int(input('Введите первое число - '))
# B = int(input('Введите второе число - '))
#
#
# def are_both_odd(A, B):
#     # return A%2!=0 and B%2!=0 - Также возможный вариант
#     return \
#             A % 2 == 1 and \
#             B % 2 == 1
#
# if are_both_odd(A, B):
#     print('Числа А и B нечетные')
# else:
#     print(are_both_odd(A, B))
#
'''Про функции
Вам нужно вместо ??? написать код, который возвращает из функции класс ветра в зависимости от его характера:

от 1 до 4 м/с включительно - "weak [1]"
от 5-10 м/c - "moderate [2]"
от 11-18 м/c - "strong [3]"
от 19 м/c - "hurricane [4]"'''

# def - объявили функцию
# get_wind_class - это мы так функцию назвали
# speed - переменная , которую мы передали в функцию get_wind_class. Выходит, что это аргумент этой функции

# speed = int(input('Введите скорость ветра - '))
# def get_wind_class(speed):
#     if (1 <=speed <= 4):
#         return "weak [1]"
#     elif (5<=speed<=10):
#         return "moderate [2]"
#     elif (11 <= speed <= 18):
#         return "strong [3]"
#     elif (speed>=19):
#         return "hurricane [4]"
# print(get_wind_class(speed))

'''Рбаота со словарём'''
'''Дан словарь - user_database
Допишите функцию check_user так, чтобы она по логину пользователя проверяла, 
существует он или нет, после чего с помощью вложенного условия проверяла
правильность пароля этого пользователя.

Функция должна возвращать только True или False.'''

# user_database = {'user': 'password',
#                  'iseedeadpeople': 'greedisgood',
#                  'hesoyam': 'tgm'}
#
# # username = input('Ввести имя пользователя: ')
# # password = input('Ввести пароль: ')
#
# def check_user(username, password):
#     if (username in user_database.keys()) and (password in user_database.values()):
#         return True
#     else:
#         return False
#
# print(check_user(username = 'user', password = '234'))

'''проверить есть ли имя пользователя в словаре.
проверить корректный ли пароль.
как?'''

# Ещё один вариант решения

# username = input('TYpe a username: ')
# password = input('Type password for username: ')
# user_database = {'user': 'password',
#                  'iseedeadpeople': 'greedisgood',
#                  'hesoyam': 'tgm'}
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
# print(check_user(username, password))


# for i in letters:
#         if i == 'a' or i == 'o' or i == 'e'\
#                 or i == 'u' or i == 'i':
#                 vowels.append(i)
#         elif i == 'y':
#                 consonants.append(i)
#                 vowels.append(i)
#         else:
#                 consonants.append(i)
# print('В списке есть гласные буквы - ', vowels, len(vowels), '\n'
# 'В списке есть согласные буквы - ', consonants, len(consonants), '\n')

# n = 3
# def print_ladder(n):
#     for i in range(1, n):
#       for
# print(print_ladder(n))

#
# def print_ladder(n):
#     for i in range(1, n+1):
#         print(i * '*')
# print_ladder(n = 3)


'''Напишите функцию print_2_add_2, которая будет складывать 2 и 2, 
а затем печатать этот результат. Не забудьте вызвать функцию, чтобы увидеть результат.'''

# def print2_add_2():
#     x = 2*2
#     print(x)
#
# print2_add_2()

'''Напишите функцию hello_world, которая будет печать приветственную строку "Hello World".'''

# def hel_wrld():
#     print('Hello world')
#
# hel_wrld()

'''Напишите функцию, которая проверяет,
является ли число n делителем числа a. И выводит на экран соответствующее сообщение,
является ли число делителем или нет.'''

# def what_is_a(a,n):
#     if a % n == 0:
#         print(n)
#     else:
#         print(not n)

'''Напишите функцию, которая печатает «обратную лесенку» следующего типа:
n = 3
***
**
*
n = 4
****
***
**
*'''
# def print_ladder(n):
#     for i in range(n,0,-1):
#         print(i * '*')
# print_ladder(4)


'''Напишите функцию, которая будет возвращать количество делителей числа а.'''
# a = 5
# def a_division(a):
#     cnt = 0
#     for i in range(1, a+1):
#         if a % i == 0:
#             cnt += 1
#
#     return cnt
# print(a_division(a))

'''Напишите функцию, которая проверяет, является ли данная строка
палиндромом или нет, и возвращает результат проверки. Пример:

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True'''

# thing = input('type some words: ')
# def if_palindrome(thing):
#     thing = thing.lower()
#     thing = thing.replace(" ", "")
#     thing = thing.replace("\n", "")
#
#     if thing == thing[::-1]:
#         return True
#     else:
#         return False
#
# print(if_palindrome(thing))


# x = 3
#
# def func():
#     global x
#     print(x)
#     x = 5
#     x += 5
#     return x
#
# print(func())

# def multpl_f(m):
#     nonlocal_m = m
#     def local_mult(n):
#         return n * nonlocal_m
#     return local_mult
# two_mul = multpl_f(2)
# print(two_mul(5))
#
# '''Про глобальные переменные внутри def'''
#
# PI = 3.14
#
# def area_circl(r):
#     global PI
#     print('output PI before mod', PI)
#     PI = 3.1415
#     print('output PI after mod inside _def_')
#     return PI * (r ** 2)
#
# print('output PI from global', PI)
# print(area_circl(15))
# print('output PI after calling _def_ and mod') # ВАЖНО! Если внутрь функции поместили переменную глобальную с помрощью _global_,
# # она может подвергнуться изменениям, что нарушит работу остальной программы, если переменная не должна изменяться.


# def mltply_any_(*numbers):
#     rslt = 1
#     for i in numbers:
#         rslt *= i
#     return rslt
# print(mltply_any_(23,7,1,140))

# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#        return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(10))
#
'''С помощью рекурсивной функции найдите сумму чисел от 1 до n.'''

# def sum_num(n):
#     if n == 0:
#         return 0
#     return n + sum_num(n-1)
#
# print(sum_num(6))

'''С помощью рекурсивной функции разверните строку'''

# def str_in_oppst(txt):
#     if len(txt) == 0:
#         return ''
#     else:
#         return txt[-1] + str_in_oppst(txt[:-1])
    # здесь сначала берём элемент из конца строки и прибавляем к нему оставшуюся строку без последнего элемемнта.


'''С помощью рекурсивной функции разверните строку.'''
# Это без рекурсии
# def str_in_opposite(txt):
#     txt = txt[:-1]
#     print(txt)
#
# str_in_opposite('asdfghjklk')


'''Дано натуральное число N. Вычислите сумму его цифр.
При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется)'''

# def summ_of_num_insd_num(N):
#     if N < 10:
#         return N
#     else:
#         return N % 10 + summ_of_num_insd_num(N // 10)
# print(summ_of_num_insd_num(100))

'''ф-ия с встроенным бесконечным генератором чисел Фибоначчи'''
# def fib():
#     a,b = 0,1
#     yield a
#     yield b
#
#     while True:
#         a,b = b, a + b
#         yield b
#
# for num in fib():
#    print(num)

'''Создайте функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать любой шаг
и любое число в качестве аргумента функции, с которого будет начинаться последовательность.'''

# def infnt_nums():
#     a = 1
#     yield a
#
#     while True:
#         a += 1
#         yield  a
#
# for num in infnt_nums():
#     print(num)

# ниже вариант с ручным вводом стартового значения и шага

# def infnt_Num(start=1, step =1):
#     counter = start
#
#     while True:
#         yield counter
#         counter += step
#
# for N in infnt_Num():
#     print(N)

'''Создайте генератор цикла,
то есть в функцию на входе будет передаваться массив, например, [1, 2, 3],
генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.'''

# def infnt_mas(*massiv):
#     inf_mas = massiv
#
#     while True:
#
#         inf_mas += massiv*2
#         yield inf_mas
#
# for i in infnt_mas(1,2,3):
#     print(i)
#
'''Или так'''
#
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)


# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()
# def hello():
#    print("Hello")
#
# twice_func(hello)
#
#
# def one_func():
#     nonlocal m

# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper(*args, **kwargs):
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
# print(my_decorator('Hello'))
#
'''Универсальный шаблон для декоратора'''
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper
#
# def abs(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
#
#
# print(abs(-8))


# def greeting(*names):
#     for name in names:
#         print('Hi, there',name+'!')
#
# greeting('John Galt', 'Jason Born','Mano Chao')

# def cnt_all(*nums):
#     sum = 0
#     for n in nums:
#         sum+= n
#     return sum
# print(cnt_all(2,3,4,5,9))


'''Сначала ф-ия декоратор с внедрением в неё основной ф-ии и возвратом значения'''
import time

# def decor_f_time(fn):
#     def wrap_f_time():
#         print(f'Здесь может быть стартовое сообщение, {fn}')
#         t_0 = time.time()
#         # ... some_variable. Здесь фактически должна лежать сама функция, которую пишем ниже.
#         result = fn()
#         fin_t = time.time() - t_0
#         print(f'''Здесь может быть завершающее сообщение с какими-либо выводами,
#               к примеру, про время выполнения функции: {fin_t}''')
#         return fin_t
#     return wrap_f_time()
#
# def pow_2():
#     return 10000000 ** 2


# def in_build_pow():
#     return pow(10000000, 2)


# pow_2 = decor_f_time(pow_2)
# in_build_pow = decor_f_time(in_build_pow)

# pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

# in_build_pow()

# def decor_time(fn):
#
#     def wrap_f_time():
#         print('Start of func - ') # put inhere a name of func
#         t_00 = time.time()
#         res = fn()
#
#         t_fin = time.time() - t_00
#         print(f'\nEnd of a func: {t_fin}') # Put a name of func
#         return res
#     return wrap_f_time()
#
# a = 100
# b = 2
# @decor_time
# def powering(a,b):
#     a = 100
#     b = 2
#     return a**b

# декоратор, в котором встроенная функция умеет принимать аргументы
# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
# @do_it_twice
# def say_word(word):
#    print(word)

# say_word("Oo!!!")
# # Oo!!!
# # Oo!!!

'''Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.'''
# def decor_counter(input_fnc):
#     counter = 0
#
#     def wrap_for_fnc(*args,**kwargs):
#         print('SMTHNG for the beginning')
#         res = input_fnc(*args,**kwargs)
#         nonlocal counter
#         counter +=1
#         print(res, 'SMTNHG for the end', counter)
#     return wrap_for_fnc
#
# @decor_counter
# def pow_2(a, b):
#    return a + b
# pow_2(4,6)
# pow_2(9,7)

'''Возьмите из предыдущего примера декорированные функции,
которые возвращают время работы основной функции и найдите
среднее время выполнения для 100 выполнений каждой функции.'''

# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
# @decorator_time
# def pow_2():
#    return 10000000 ** 2
#
# @decorator_time
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for r in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")
# print(pow_2())


'''Универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper
    
    '''


'''
Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре. 
Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается 
аргумент функции, по значению результат работы функции, например, {n: f(n)}.

И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
То есть словарь можно считать промежуточной памятью на время работы программы,
где будут храниться ранее вычисленные значения. Исходная функция,
которую нужно задекорировать имеет следующий вид и выполняет
простое умножение на число 123456789:

def f(n):
   return n * 123456789
   '''


# def decor_f_mltply(fn):
#     print(f"Star of function {fn}")
#     res_dict_f_func = {}
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal res_dict_f_func, count
#         print(f'\nЭтот код будет выполняться перед каждым вызовом функции {fn}')
#         count += 1
#         result = fn(*args)
#         for key in range(count):
#             res_dict_f_func[str(*args)] = fn(*args)
#         print(f'\nResult for {fn} - {result}'\
#               f'\nResult is put into dict {res_dict_f_func}')
#         print('\nЭтот код будет выполняться после каждого вызова функции')
#     return wrapper
#
# @decor_f_mltply
# def f_mltply(n):
#    return n * 123456789
#
# f_mltply(2)
# f_mltply(3)
# f_mltply(10)
# f_mltply(4)


'''
Возможное решение задчаи со словарём:

def cache(func):
   cache_dict = {}
   def wrapper(num):
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кэш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кэша: {cache_dict[num]}")
       print(f"Кэш {cache_dict}")
       return cache_dict[num]
   return wrapper
'''

'''
Напишите рекурсивную функцию, находящую минимальный элемент
списка без использование циклов и встроенной функции min().
'''

# L = [i for i in range(15,50,5)]
# print(L)
# print(L[1:])
# J = 354
# print(len(str(J)))


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


# iter_obj = iter("Hello!")
#
# print(next(iter_obj))

'''рекурсивная функция, которая зеркально разворачивает число.
Предполагается, что число не содержит нули.'''
# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)


'''
функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S.
При написании программы следует обратить внимание на то,
что, если S стала отрицательной, то необходимо сразу вернуть False.
'''

# def equal(N,S):
#     if N < 10:
#         return N
#     else:
#         return N % 10 + summ_of_num_insd_num(N // 10)

# L = list(map(int, input('type: ').split()))
# print(L)
'''
Вот,что на выходе:
type: 5 5 9 6 64 45
[5, 5, 9, 6, 64, 45]
'''

# N = 25
# S = 7
# sum_N = N % 10
# print(sum_N)
# def if_N_eq_S(N):
#     global S
#     sum_N = 0
#     if sum_N == S:
#         return f'N{N} в сумме чисел {sum_N} равен {S}'
#     else:
#         return sum_N + (if_N_eq_S(N % 10))

# if_N_eq_S(N)

'''
вычисление, равна ли сумма чисел в "Н" и цифре в "С".
фктически делим с остатком на 10 "Н" и остаток вычитаем из "С". 
Сравниваем "Н" и "С", когда "Н" - однозначное, т.е. меньше 10. Если не равны, значит сумма не совпала
Значит Враки.
N = 255
S = 12
def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)
print(equal(N,S))
'''




'''генератор для приближенного вычисления числа e = 2.718.
Для нахождения числа, удовлетворяющего необходимой точности будем использовать следующий цикл: (ниже, под комментами)

e_n = (1 + 1/n)**n, В этой формуле число n — натуральное (1, 2, 3 и т. д.).'''

'''

def e(): # формула вычисления числа определённой точности в генератор размещаем формулу.
    n = 1
    while True:
        yield (1 + 1/n) ** n
        n += 1

last = 0
for a in e(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение

'''



'''
здесь декоратор для проверки авторизации.
Если авторизация Верняк, то запускаем функцию, какую хотим, если Враки, то сообщение о том,
что нет авторизации. 

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
    print("some data from database")

from_db()

'''



'''
Реализуйте функцию-декоратор, которая проверяет доступ к функции по username пользователя.
Все username пользователей хранятся в глобальной области видимости в списке USERS.
При согласии пользователя на авторизацию ему предлагается ввести username,
который также хранится в глобальной области видимости. Функция должна использовать два декоратора:
один для проверки авторизации вообще (реализован выше), второй — для проверки доступа.
'''

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
# def is_auth(func):
#     def wrapper():
#         global USERS
#         if auth:
#             print("Пользователь авторизован")
#
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
# def has_access(func):
#     global USERS
#     def wrap_for_acces():
#         if auth:
#             is_user = input('Введите имя пользователя: ')
#             if is_user in USERS:
#                 print('пользователь имеет доступ')
#                 func()
#             else:
#                 print('Root access failed. Access denied')
#
#     return wrap_for_acces
#
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()

# a_list = [1,4,9]
# print(list(map(pow_, a_list)))  # [1, 4, 9]

L = ['THIS', 'IS', 'LOWER', 'STRING']
a_list = ['FT', 'SDXC', 'POI']
# print(list(map(str.lower, L)))

# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))


line = [-2, -1, 0, 1, -3, 2, -3,4]
# def pos(x):
#     return x > 0

# print(pos(-9))

# pos_numb = list(filter(pos, line))

# print(pos_numb)


# def num_is_odd(fnc):
#         if (fnc % 2) == 0:
#             return True
#         else:
#             return False
#
# odd_line = list(filter(num_is_odd, line))
# print(odd_line)


# another_list = [i - 10 for i in range(1,20,2)]
# print(another_list)
#
# def pow_2(x): return x*2
# def posit(x): return x > 0
#
# # print(list(map(pow_2, filter(posit, another_list))))
# #
# # K = [i * 2 for i in another_list if i > 0]
# # print(K)
#
# print([pow_2(i) for i in another_list])
#
# print(list(map(pow_2, another_list)))
#
# print([pow_2(i) for i in another_list] == list(map(pow_2, another_list)))

d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# print(sorted(d.items())) # вернёт список кортежей из пар ключ/значение
# print(dict(sorted(d.items()))) # сортирует в вид словаря по ключам
# print(d.keys(), d.values())
# print(d.keys())
# print(dict(sorted(d.items(), key=lambda x: x[1])))
'''
А вот чтобы отсортировать словарь по значениям, необходимо указать,
что сортировать нужно по второму элементу кортежа ключ-значение.
Тут на помощь приходят lambda-функции. У встроенной функции sortred()
можно задать аргумент key, который укажет, по какому ключу нужно производить сортировку.

sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря
'''

'''
Предположим у нас есть список с данными о росте и весе людей.
Задача — отсортировать их по индексу массы тела. 
Он вычисляется по формуле: рост в метрах возвести в квадрат,
потом массу тела в килограммах разделить на полученную цифру.
m \ h **2, где h  метрах
'''
# (вес, рост)
'''data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
 ]
print('0 (original data): ', data)

print('1 (sorted tuple with dict and lambda): ', sorted(data, key=lambda x: x[0] / (x[1] / 100) ** 2))
print('1.1 (min value for data by IMT): ', min(data, key=lambda x: x[0] / (x[1] / 100) ** 2))

print('2 (printed item in tuple): ', *data[0])

for m,h in data:

    new_data = {
        key:value
        for key, value in zip(data, [m / ((h / 100) ** 2) for m,h in data])
    }

print('3 (index massi tela + new dict with IMT and old data tuple: ', '\n','\n',
      new_data)'''

# a = ["asd", "bbd", "ddfa", "mcsa"]
#
# print(list(map(len, a)))
#
# a_1 = ["это", "маленький", "текст", "обидно"]
#
# print(list(map(str.upper, a_1)))
# def IMT(func):
#     for m, h in data:
#         return m / ((h / 100) ** 2)


# data_dict = dict(sorted(data, IMT))

# print(data_dict)



# print(data[0][0])
# print(dict(sorted(data)))


# data_sort = list(map(IMT, dict(data)))
# print(data_sort)
# print(dict(sorted(data), key == lyambda(x): key/(values/100)**2))


'''Создать обработчик задач'''

# queue_of_task.append(input('What to do? - Write it down! \n---'))
'''
length_of_task_line = int(input('Ввести длинну списка задач: '))
queue_of_task = [0 for _ in range(length_of_task_line)] #список для контроля длины и обработки задач
order = 0 #номер задачи
head_of_que = 0
tail_of_que = 0
def is_empty():
    return head_of_que == tail_of_que and queue_of_task[head_of_que] == 0
def size(): #current size of queue
    if is_empty():
        return 0
    elif head_of_que == tail_of_que:
        return length_of_task_line
    elif head_of_que > tail_of_que:
        return length_of_task_line - head_of_que + tail_of_que
    else:
        return tail_of_que - head_of_que
def add():
    global order, tail_of_que
    order += 1
    queue_of_task[tail_of_que] = order
    print(f'Task N_{order} is added to the list')
    tail_of_que = (tail_of_que + 1) % length_of_task_line
def do():
    global head_of_que
    print(f'Task N_{queue_of_task[head_of_que]} is done and deleted')
    queue_of_task[head_of_que] = 0
    head_of_que = (head_of_que + 1) % length_of_task_line
while True:
    cmd = input('Введите команду: ')
    if cmd == 'empty':
        if is_empty():
            print('List is empty')
        else:
            print('List is not empty')

    elif cmd == 'size':
        print('Amount of tasks in the queue: ', size())

    elif cmd == 'add':
        if size() != length_of_task_line:
            add()
        else:
            print('List is full.')

    elif cmd == 'show':
        if is_empty():
            print('List is empty.')
        else:
            print(f'Task N_{head_of_que} is in priority')

    elif cmd == 'do':
        if is_empty():
            print('List is empty.')
        else:
            do()

    elif cmd == 'exit':
        for _ in range(size()):
            do()
        print('Queue is empty. End.')
        break
    else:
        print('Wrong command')


# queue_of_task[4] = 4
# print(queue_of_task[head_of_que])
# print(queue_of_task[head_of_que] == 0)'''

