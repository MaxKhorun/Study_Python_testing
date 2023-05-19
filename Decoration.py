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


Вот универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper