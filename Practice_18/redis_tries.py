import redis
import json

red = redis.Redis(
        host= 'redis-16359.c302.asia-northeast1-1.gce.cloud.redislabs.com',
        port= 16359,
        password= 'q1B6SzXWcggdeWASQtomzyHMEzkZOs29'
)

phone_book = {}

# name = input('Type a name for the phone book: ')
# telephon = input('введите нмер телефона: ')
# red.set(phone_book)
# red.get(phone_book)
def phone_book_filler():
        global phone_book
        phone_book[input('Type a name for the phone book: ')] = input('введите номер телефона: ')
        red.set('phone_book', json.dumps(phone_book))
        return phone_book
phone_book_filler()
phone_book_filler()
print(red.get('phone_book'))

'''red = redis.Redis(
    host='ваш хост', 
    port=ваш порт, 
    password=пароль 
)
 
cont = True
 
while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break'''
#         name = input('Type a name for the phone book: ')
#         telephon = input('введите нмер телефона: ')
#         print(telephon, type(telephon))
#
#         phone_book[name] = telephon