# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#
# for t in per_cent.items():
# for t in per_cent.keys():
# for t in per_cent.values():
#     print(t) - циклом пройтись по словарю и достать значения, ключи или пары.


# a = [(1,2,),(3,4,)]
# for x, i in a:
#     print('Value for x - ', x)
#     print('Value for i - ', i)
# print(a[0], type(a[0])) -- Работает, только если совпадает кол-во переменых и введённых значений

# m = [[23,45,67],[6,7,2],[3,67,90]]
#
# for item in m:
#     print(it)


# list = [int(x) for x in range(30,81,3)] - цикл внутри объявлении переменной списка.
# print(list)

# list = [str(x) for x in range('a','z')]
# print(list) - здесь будет ошибка, т.к. это не по правилам языка.

# a = -10
# if a < 0:
#     print('Hello')
# else:
#     print('Mistake')

# D = 3 # могу ввести количество билетов и исходя из этого кол-ва создать словарь.
# tickets = dict.fromkeys(i for i in range(1,D+1)) # не могу наполнить его правильно.
# print(tickets)
#
# cost_f_ticket = []
# N = int(input('Введите желаемое кол-во билетов: '))
# T = {'Посетитель '+str(n): int(input('Введите возраст посетителя : ')) for n in range(1,N+1)}
# # ^^ Здесь сразу создание словаря с порядковыми номерами Посетителей и возраста к ним.
#
# for age in T.values():
#     if age < 18:
#         cost_f_ticket.append(0)
#     elif 18 <= age < 25:
#         cost_f_ticket.append(990)
#     elif age >= 25:
#         cost_f_ticket.append(1390)
#
# tickets = {key:value
#            for key, value in zip(T.keys(),cost_f_ticket)}
# print(tickets, '\n',sum(tickets.values())-(sum(tickets.values())*0.1))

# cost_range = [{'до 18': 0, 'от 18 до 25': 990, 'старше 25': 1390}, {'от 3-х билетов': 0.1}]
# summa = []
# cnt_tick = ['Посетитель ' + str(i) for i in range(1, int(input('Введите желаемое кол-во билетов: ')) + 1)]
# age_visitors = [int(input('Введите возраст посетителя через пробел: ')) for i in range(len(cnt_tick))]
# print(cnt_tick)
# print(age_visitors)
#
# for age in age_visitors:
#     if 18 <= age < 25:
#         summa.append(990)
#     elif age >= 25:
#             summa.append(1390)
#     elif age < 18:
#         summa.append(0)
#
# tickets = {key:value
#            for key, value in zip(cnt_tick,summa)}
# print(tickets, '\n',sum(tickets.values())-(sum(tickets.values())*0.1))


# оператор распаковки _*_ перед переменной

# a = [1,2,3]
# b = ['a','d','v']
# b = [*b,*a]
# print(b)

# конструкции *args , **kwargs для того ,чтобы функция
# могла принимать неограниченное кол-во позиционных и именованных аргументов

# dict = {}
# print(dict)
#
# n=3
#
# for key in range(1,n+1):
#     dict['key '+str(key+1)] = key
# print('\n',dict)


# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b:
#         return 'Бесконечное количество корней'
#     else:
#         return 'Нет корней'
# print(linear_solve(0,0))
'''
Решение квадратного уравнения
'''
import random

# def discriminant(a,b,c):
#     return (b**2) - (4 * a * c)
#
#     # if ((b**2) - (4 * a * c)) > 0:
#     # else:
#     #     return 'Нет вещественных корней'
#
# def quadratic_solve(a,b,c):
#     if discriminant(a,b,c) < 0:
#         return 'Нет вещественных корней'
#     elif discriminant(a,b,c) == 0:
#         return f'У уравнения единственный корень {(-b/(2*a))}'
#     else:
#         return ((-b - discriminant(a,b,c)**0.5) // (2 * a)), ((-b + discriminant(a,b,c)**0.5) // (2 * a))
#     # else:
#     #     return discriminant(a,b,c)

'''Распаковка данных'''
# M = {'a' : 1,
#      'b' : 0,
#      'c' : -1}
#
# print(*M) # Есть ещё оператор **, но он не сработал, как в модуле.
# print(*M.values())

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# G = input('input your Username: ')
#
# if G in USERS:
#     print(bool(G))
# else:
#     print(not G)


# def adder(x):
#     print(x+5)
#
# adder(15)

import math
'''def result_in_dict(fnc):
    results = {}
    count = 0
    def wrapper_inside_fnc(*nums):
        nonlocal count
        if nums not in results:
            results[*nums] = fnc(*nums)
            print(f'Write value in: {results[*nums]}')
        else:
            print(f'Return values from temp dict_mem: {results[*nums]}')
        print(f'Dict_mem: {results}')
        count +=1
        print(count)
    return wrapper_inside_fnc

@result_in_dict
def nums(a,b,c):
    return (a+b)*c/2

nums(2,3,4)
nums(1,5,9)
nums(10,23,5)
nums(2,3,4)
nums(2,3,4)'''

#
# alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
# alphabet_upper = alphabet.upper()
# eng_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
# eng_alphabet_upper = eng_alphabet.upper()
#
# code_num = int(input('Введите число для создания шифрованной версии текста: '))
# encoded_sum = ''
# def char_in_text_plus(txt):
#     for item in txt:
#         if item in alphabet:
#             return alphabet[(alphabet.index(item) + code_num) % len(alphabet)]
#         elif item in alphabet_upper:
#             return alphabet_upper[(alphabet_upper.index(item) + code_num) % len(alphabet_upper)]
#         else:
#             return item
#
# with open('D:\SF\Цезарь.txt','r', encoding='utf8') as m_file:
#     for line in m_file:
#         for item in line:
#             encoded_sum += char_in_text_plus(item)
# # print(encoded_sum)
#
# with open('Encoded output.txt', 'w', encoding='utf8') as final_file:
#     final_file.write(encoded_sum)
# a,f,j,y = 3, 1, 1, 0
# L = [3,7,2,0]
# for i in L:
#     if all(i) is int:
#         print(L)
#     else:
#         print('no int')

# rand_L = random.choice(range(left, right))
# print(rand_L)
# if L[M] == s_N:
#     print(M, f'число - {L[M]}')
# else:
#     print('Nope', M, f'число - {L[M]}')
currency_dict = {
    'рубли': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'фунт стерлингов': 'GBP',
    'японская йена': 'JPY',
    'китайский юань': 'CNY'
}

text = 'Доступные валюты для перевода: '
for k in currency_dict.keys():
    text = '\n'.join((text, k,))

# print(text)