# Function as a type

def say_hello():
    print('Hello')
def say_goodbye():
    print('Good Bye')

# message = say_hello
# message()
# message = say_goodbye
# message()
#переменной можно присвоить имя функции и потом переменную вызыввать, как функцию!

# def sum(a,d):
#     return a+d
# def mult(a,d):
#     return a*d
# operation = sum
# result = operation(5,6)
# print(result)
#
# operation = mult
# print(operation(5,6))

# recursion.

# def rec(x):
#     if x< 4:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(1)

# факториал числа$ 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 =
# n! = 1 * ... * (n-2)*(n-1)*n

# def fact(x):
#     if x ==1:
#         return 1
#     return fact(x-1)*x
# print(fact(4))


# определить чётное число$ with recurcion def
# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return check(n-2)
# n = int(input('Type a numb: '))
# if (check(n)==True):
#     print('Число чётное')
# else:
#     print('число нечётное')

# a = [i ** 2 for i in range(1, 6)]
# print(a)
#
# a = ['2', '5', '5']
# # a_mod = list(map(int, a))
# a_mod = [int(i) for i in a]
# print(a_mod)

# выражение-генератор
# генератор - это итератор, элементы коротого можно итерировать только один раз
# итератор - это объект, который поддерживает ф-ию next(), а также помнит о том, какой элемент
# будет браться следующим.

'''итерируемый объект - объект, который педоставляет возможность пройти поочередно сови элементы'''

#iter

'''s = [1,2,3]
d = iter(s)
print(next(d))
print(next(d))
print(next(d))
# print(next(d))'''

# a = (i ** 2 for i in range(1, 6))
# print(next(a))
# print(next(a))

'''генераторы не сохраняют данные в память - формируют на лету и забывают.
позвонляют проитерировать свои элементы один раз; потому что не сохраняют в память.
Используются, когда в программах есть много данных'''

# yield превращает обыяную ф-ию в генератор
# return
# def cube_numbers(nums):
#     cube_list =[]
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
#
# print(cube_numbers([1, 2, 3, 4, 5]))


'''def cube_numbers(nums):

    for i in nums:
      yield (i**3)
cube = cube_numbers([1,2,3,4,5])
print(next(cube))
print(next(cube))
print(next(cube))'''

# декораторы
#
#

# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
#
# def my_func():
#     print('here is the main text & func')
#
# # my = my_decor(my_func)
# # my()
#
# @my_decor
# def my_func(num):
#     print(num**2)
# my_func(4)

