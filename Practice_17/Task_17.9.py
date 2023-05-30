'''
3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
а следующий за ним больше или равен этому числу.

При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска,
который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

Подсказка
Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
В этом случае необходимо вывести соответствующее сообщение'''

import random
def type_numb():
    global N
    try:
        N = int(input('Введите число для работы программы: '))
        if N or N==0:
            return N
    except ValueError as error:
            print(error)
            print('Вы ввели неправильное значение.')
    return type_numb()
def list_check():
    try:
        L = list(map(int, input('Введите числа через пробел: ').split()))
        if L:
            L.append(type_numb())
            return L
    except ValueError as error:
        print(error)
        print('Повторите ввод')
        return list_check()
def sort_an_L(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = sort_an_L(L[:middle])
        right = sort_an_L(L[middle:])
        return merge(left, right)
def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result
def studing_binary(L, N):
    left = 0
    right = len(L)-1
    while (left <= right):

        M = (left + right) // 2
        if L[M] < N and L[M+1] >= N:
            return \
                f'full list: {L}'\
                f"\nindex: {M}, number itself: {L[M]},"
        elif L[M] == N:
            return \
                f'full list: {L}'\
                f"\nindex: {M-1}, number itself: {L[M-1]},"
        elif L[0] == N:
            return f'Number is a beggining of a list: {N}.' \
                   f'\nfull list: {L}'
        elif L[M] > N:
            right = M
        elif L[M] < N:
            left = M+1
    return "It is not here. Try again."

N = None
L = list_check()
result = studing_binary(sort_an_L(L), N)
print(result)

