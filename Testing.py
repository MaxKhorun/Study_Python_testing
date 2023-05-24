# Test methods

# class test:
#     def assert_equals(a,b):
#         assert (a == b)

'''Даночисло n. C начала суток прошло n минут.Сколько часов и минут будут показывать электронные часы в этот момент. 
Нужно два числа: колво часов от 0 до 23 и кол-во минут от 0 до 59.
n может быть больше, чем минут в сутках'''

# def electr_clck(num):
#     minutes = num % 60
#     hours = (num // 60) % 24
#     return str(hours)+' '+str(minutes)
#
# print(electr_clck(300), type(electr_clck(300)))

'''Написать код, который будет рассчитывать угол между
часовой и минутной стрелкой в заданное время'''

# from datetime import datetime - библотека, которая работает со временем.
# h = arg.hours - аргумент, который возращает значение часа.
# m =arg.minutes - аргумет библиотеки,который возвращает значение минут.

'''Binar search. Game "Guesss the number" '''
'''number = int(input('type: '))
def guess_the_N(number):
    counter = 1
    minimum = 1
    maximum = 100
    predict = (minimum + maximum) // 2
    while predict != number:
        counter += 1
        if predict > number:
            maximum = predict
        else:
            minimum = predict
        predict = (minimum + maximum) // 2
    return counter

print(guess_the_N(number))'''

'''lbrnth = []

with open(f'C:\SF\GITHUB\Study_Python_testing\labirinth.txt', 'r') as file:
    for line in file:
        lbrnth.append(line.replace('\n', '').split(' '))
print(lbrnth)
for i in range(len(lbrnth)):
    for y in range(len(lbrnth)):'''


fff = ['dfg', {'sdf': None}, {3: [3, 3], 8:[2, 12], 'sdf':None}, {4: [4, 6, 9]}, 'w sed', 2, 'sdf']

print(fff[2][8])
