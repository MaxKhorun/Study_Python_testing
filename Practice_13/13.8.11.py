'''Напишите программу, которая на вход принимает
последовательность целых чисел,
и возвращает True, если все числа ненулевые,
и False, если хотя бы одно число равно 0.'''

print('Введите 5 целых чисел.')
nums = [3,-4,5]
# while len(nums)<4+1:
#     nums.append(int(input('')))
print('Ваши введённые числа: ', nums)

for i in nums:
    if i == 5 and i > 0:
        print('ok')
    elif i < 0:
            print('not OK')







