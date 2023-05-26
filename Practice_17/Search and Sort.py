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


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))'''


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

array = [2, 5, 1, 4, 6, 5, 9, 8, 7]

# for i in range(len(array)):
#     frst_indx = i # его сравниваем со всеми остальными
#     for j in range(frst_indx, len(array)):
#         if frst_indx > j:
#             frst_indx = j
#         elif frst_indx == j:

for i in range(1, len(array)):
    x = array[i]
    idx = i
    count = 0
    while idx > 0 and array[idx-1] > x:

        array[idx] = array[idx-1]
        idx -= 1
    count += 1
    array[idx] = x

print(array)
print(count)