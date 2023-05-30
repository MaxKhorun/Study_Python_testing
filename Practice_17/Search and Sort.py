'''# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i, array[i]
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
#
# def count_element(array):
#
#
#         set(array)
#         return len(set(array))
def count_elem(array, elem):
    count = 0
    for i in array:
        if i == elem:
            count +=1
    return count

array = (list(i for i in range(0,11)))*2

print(count_elem(array, 6))
'''

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input('put a numb: '))
array = [2, 5, 1, 4, 6, 5, 9, 8, 7]

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, len(array)))


'''# Naive
import random

array = [i for i in range(0,10)]

is_sort = False
count = 0
while not is_sort:
    count +=1

    random.shuffle(array)

    is_sort = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_sort = False
            break
# print(array)
# print(count)'''

'''def fact(i):
    if i == 1:
        return 1
    return fact(i-1)*i

f = fact(100)
print(f)
print(len(str(f)))'''

'''array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):
    indx_min = i

    for j in range(i, len(array)):
        count += 1
        if array[j] < array[indx_min]:
            indx_min = j

    if i != indx_min:

        array[i], array[indx_min] = array[indx_min], array[i]


print(array)
print(count)'''

#Сортировка выбором \ selection sorting

'''array = [2, 3, 1] #4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):
    indx_max = i

    for j in range(i, len(array)):
        count += 1
        if array[j] > array[indx_max]:
            indx_max = j

    if i != indx_max:

        array[i], array[indx_max] = array[indx_max], array[i]


print(array)
print(count)'''

'''array = [2, 5, 1, 4, 6, 5, 9, 8, 7]


# сортировка вставками
# |
# |
# V
count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i

    while idx > 0 and array[idx-1] > x:
        count += 1
        array[idx] = array[idx-1]
        idx -= 1

    array[idx] = x

print(array)
print(count)'''


#Пузырьковый метод

'''array = [2, 5, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)'''


#сортировка слиянием

'''L = [2, 5, 1, 4, 6, 5, 9, 8, 7]

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(L))'''

#быстрая сортировка
import random

'''array = [2, 5, 1, 4, 6, 5, 9, 8, 7]

def qsort(array, left, right):
    middle = left+right // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array
'''


'''L = [2, 5, 1, 4, 6, 5, 9, 8, 7]

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(L))'''