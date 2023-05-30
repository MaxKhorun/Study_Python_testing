# a=15
# if a>5:
#     a=5
# a=a+2
# print(a)

# a = 11
# if a < 6:
#     a = a+13
# else:
#     a = a-8
# print(a)
#
# a = 7
# b = 9+a
# print("a=F(",b,")")
#
#
# a = 16
# b = 14 + a
# print("b=",b)


# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
#
# b = 7
# b /= b
#
# if x > mx:
#     mx = x
#
# print(s)
# print(mx)

# is_rainy = True
# heavy_rain = False
#
# if is_rainy:
#     if heavy_rain:
#         print('Брать зонт')
#     else:
#         print('Надеть дождевик')
# else:
#     print('Не брать зонт')

# zero = 3
# if zero:
#    print(10 / zero)
# else:
#    print("Делить на ноль нельзя")

# #
# '''Проверка целого числа А'''
#
# A = int(input('Введите число - '))
# if (A % 2 == 0) or (A % 3 == 0):
#     print(A, 'Число кратно 2-м и 3-м')


# '''Проверка времени суток'''
#
# hour = int(input('Веедите значение часа - '))
#
# if 6 <= hour < 12:
#     print('Сейчас утро')
# elif 12 <= hour < 18:
#     print('Day time!')
# elif 18 <= hour < 23:
#     print("It's evening time'")
# else:
#     print("It's night, my friend'")

# x = int(input('Enter something for X: '))
# y = int(input('Enter something for Y: '))
#
# if x > 0 and y > 0:
#     print('I')
# elif x < 0 and y > 0:
#     print('II')
# elif x < 0 and y < 0:
#     print('III')
# else:
#     print('IV')

'''Определите сезон в зависимости от номера месяца и выведите сообщение:'''
# month = int(input('Введите номер месяца - '))
#
# if month in [12,1,2]:
#     print('Zima')
# elif month in [3,4,5]:
#     print('Vesna')
# elif month in [6,7,8]:
#     print('Leto')
# elif month in [9,10,11]:
#     print("Osen'")
# else:
#     if month or (month==0):
#         print('Попробуйте заново ввести номер месяца от 1 до 12')

''' letter = input('Введите латинскую букву: ')
if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
    print('Гласная буква')
elif letter == 'y':
    print('Это гласная и согласная буква')
else:
    print('Согласная буква;', type(letter))
    '''
# То же самое со списком:
# count, letters, vowels, consonants = 0, [], [], []
# while count <=9:
#         letters.append(input('Введите 10 латинских букв: '))
#         count +=1
#
# print('Весь список введённых букв - ', letters)
#
#
# for i in letters:
#         if i == 'a' or i == 'o' or i == 'e'\
#                 or i == 'u' or i == 'i':
#                 vowels.append(i)
#         elif i == 'y':
#                 consonants.append(i)
#                 vowels.append(i)
#         else:
#                 consonants.append(i)
# print('В списке есть гласные буквы - ', vowels,'\n'
# 'В списке есть согласные буквы - ', consonants, '\n')



# if letter == 'a' or letter == 'e' or letter == 'i' \
#         or letter == 'o' or letter == 'u':
#     print('Гласная буква')
# elif letter == 'y':
#     print('Это гласная и согласная буква')
# else:
#     print('Согласная буква;', type(letter))

# numb = int(input('Введите любое целое число: '))
#
# if numb % 2 == 0:
#         print(f'Вы ввели чётное число - {numb}')
# elif numb % 2!= 0:
#         print(f'Вы ввели нечётное число - {numb}')
# else:
#         print('Вы ввели что-то не то')


# heads = 35
# leg = 94
#
# # rab - rabbits
# # ph - phazans
#
# for rab in range(heads):
#     for ph in range(heads):
#         if (rab + ph) > heads or \
#                 (4 * rab + 2 * ph) > leg:
#             continue
#         if (rab + ph) == heads and \
#                 (4*rab + 2*ph) == leg:
#             print(rab, ' - кроликов;\n',
#       ph, '- фазанов')

'''a = 0
b = False

if a and b:
    print('Обе переменные истинны')
    print(a,', ',b)
elif a or b:
    print('Истинна только одна - ')
    print(a or b)
else:
    print('Обе переменные ложные')'''


'''Представим, что на вход нашей программы подается число. 
А мы хотим проверить, является ли оно целым, находится ли в определенном промежутке 
(например от 100 до 999 включительно), да еще и делится ли на 2 и 3 одновременно. 
Очень много условий. И такое случается в реальных проектах.

Решение в лоб — использовать вложенные условные операторы. 
Один if внутри другого if и так далее. Наверняка есть способ сделать это быстрее и эффективнее, 
но для начала попробуем написать решение в таком варианте, чтобы было с чем сравнить:
'''
# a = 996
#
# if type(a) == int and (a in range(100, 999 + 1)) and (a % 2 == 0) and (a % 3 == 0):
#     print('число удовлетворяет')
# else:
#     print(not a)

# a = 996
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print('Число удовлетворяет hfp', bool(a))
# else:
#     print(not a)

# a = 999
# if any([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print('Число удовлетворяет hfp', bool(a))
# else:
#     print(not a)

    # aaabbccccdaa - подаётся такая последовательность.
    # a3b2c4d1a2 - должна такая

# stroka = 'aaabbccccdaaddcc'
# cnt = 0
# pervii_znak = stroka[0] # сохраняем первый символ
# result = ''
#
# for l in stroka:
#      if l == pervii_znak: # если символ совпадает с сохраненным,
#          cnt += 1 # то увеличиваем счетчик
#      else:
#          result += pervii_znak + str(cnt) # иначе - записываем в результат
#          pervii_znak = l # и обновляем сохраненный символ с его счетчиком
#          cnt = 1
# result += pervii_znak + str(cnt)
# print(result)

# a = 'aa'
# b = 'a'
# c = a.count('a')
# print(c)
# print(type(str))
# str_n = [i for i in stroka]
# str_nn = [i for i in stroka]
# cnt = [a+b for a,b in zip(str_n,str_nn)]
# print(cnt)
# # str_3 = stroka.split('') - это не сработало, так как последовательность без разделителей.
# for i in str_n:
#     if i == 'a':
# #         count_a +=1
# print(str_n.count('a'))
# # str_2 = ''.join(str_n)
# # print(str_2)
# L = list(map(int, input().split()))


# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!")
# #
# try:
#     x = int(input('введите число/числа - '))
#     print(x)
# except ValueError as error:
#     print(error)
#     print('Введите число заново')
# else:
#     print(f'Вы ввели правильное число - {x}')
# finally:
#     print('Выход из программы')

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        counter += 1
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x
print("количество сравнений:", counter)
print(array)