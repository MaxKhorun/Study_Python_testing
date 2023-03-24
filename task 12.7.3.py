
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# percents = list(per_cent.values()) Сначала хотел перевести в список значения словаря, чтобы там с ними работать.
# print(type(percents[0])) - здесь хотел понять, в каком формате добавились в список значения словаря; в образовательных целях =).
''' print(type(per_cent.get('ТКБ'))) Не был до конца уверен, что тип данных, как мне нужен, 
f потом вспомнил, что Python сам проводит идентификацию типов... =)'''

deposit = list()
inp_depo = int(input('Ведите желаемую сумму для внесения на депозит: '))

for keys in per_cent:
    deposit_add = deposit.append(int(inp_depo*per_cent[keys]))
print('Возможные суммы дохода: ', deposit)
print('Максимальная сумма, которую Вы можете заработать - ', max(deposit))


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# percents = list(per_cent.values()) Сначала хотел перевести в список значения словаря, чтобы там с ними работать.
# print(type(percents[0])) - здесь хотел понять, в каком формате добавились в список значения словаря; в образовательных целях =).
''' print(type(per_cent.get('ТКБ'))) Не был до конца уверен, что тип данных, как мне нужен, 
f потом вспомнил, что Python сам проводит идентификацию типов... =)'''


'''Это второй способ, который захотелось реализовать, т.к. подумалось, 
что вывод в виде словаря с ключами - просто понятнее немного. =)'''

deposit_money = list()
keys_dict = per_cent.keys()
inp_depo = int(input('Ведите желаемую сумму для внесения на депозит: '))

for keys in per_cent:
    deposit_add = deposit_money.append(int(inp_depo*per_cent[keys]))

deposit = {key:value
           for key, value in zip(keys_dict,deposit_money)}
print('Возможные суммы дохода:\n',deposit)
print('Максимальная сумма, которую Вы можете заработать - ', max(deposit_money))

