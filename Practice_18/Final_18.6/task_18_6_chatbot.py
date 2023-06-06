import telebot
import requests
import json


'''https://api.currencylayer.com/convert?access_key=547f271af5b293a46558b6c617c7088c&from=USD&to=GBP&amount=10
   ? access_key = 547f271af5b293a46558b6c617c7088c
   &from=USD
   &to=GBP
   &amount=10'''

'''7e0f586fe9a958fe6a6cda3c07537e4507ea88afeb3745bec67220000197fdcd'''

TOKEN = '6050867287:AAGGG2blD609bc8ELrquhAoWcJA-ITtsd0w'

currency_Bot = telebot.TeleBot(TOKEN)
currency_dict = {
    'рубли': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'фунт стерлингов': 'GBP',
    'японская йена': 'JPY',
    'китайский юань': 'CNY'
}
@currency_Bot.message_handler(commands=['start'])
def bot_start(message):
            text = 'Привет! Вы запустили бот-помошник для конвертации валют. \
            Список доступных команд можете уведить набрав команду: /help'
            currency_Bot.send_message(message.chat.id, text)
@currency_Bot.message_handler(commands=['help'])
def help_cmnd(message):
    text = 'Чтобы сконвертировать валюту по текущему курсу, введите:' \
           '<валюта, из которой переводим>,< валюта в кторую переводим>, <количество единиц валюты>.' \
           'Список валют для конвертации: /currencies'
    currency_Bot.send_message(message.chat.id, text)
@currency_Bot.message_handler(commands=['currencies'])
def curency_rates(message):
    text = 'Доступные валюты для перевода: '
    for k in currency_dict.keys():
        text = '\n'.join((text, k, ))
    currency_Bot.send_message(message.chat.id, text)

'''@currency_Bot.message_handler(content_types=['text'])
def convertion(message):
    from_, to_, amount = message.text.split(' ')
    req_API = requests.get(f'https://api.currencylayer.com/convert?access_key=547f271af5b293a46558b6c617c7088c&from={currency_dict[from_]}&to={currency_dict[to_]}&amount={amount}')
    result = json.loads(req_API.content)[currency_dict[to_]]
    text_res = f'количество {amount} {from_} в {to_} = {result}'
    currency_Bot.send_message(message.chat.id, text_res)'''

@currency_Bot.message_handler(content_types=['text'])
def check_rates(message):
    from_, to_, amount = message.text.split(' ')
    req_API = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currency_dict[from_]}&tsyms={currency_dict[to_]}')
    result = json.loads(req_API.content)[currency_dict[to_]]
    text_res = f'количество {amount} {from_} в {to_} = {result, type(result)}'
    currency_Bot.send_message(message.chat.id, text_res)

currency_Bot.polling(none_stop=True)