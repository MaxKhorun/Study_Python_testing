import math

# n = 10000
#
# res = math.log2(10000)
# print(res)
# n_1 = n**2
# print(n_1)
# print('---')
# print(round(n_1/(n*res)))

# summa = (1 + 100)/2 * 100
# print(summa)
# print(sum(i for i in range(1,100+1)))

# def infinite(x):
#
#     if x == 0:
#         return
#     else:
#         infinite(x-1)
#         print(x)
#
# print(infinite(5))


'''def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack[s] = s # добавляем её в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0

print(par_checker('(5+6)*{7+8}/[4+3]'))'''

