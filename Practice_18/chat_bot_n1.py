import telebot
import lxml.html
from lxml import etree


token_01_06_23 = 'None'

test_bot = telebot.TeleBot(token_01_06_23)

@test_bot.message_handler(commands=['start'])
def start_n_help_func(message):
    test_bot.send_message(message.chat.id, f'Hello, there, pal, {message.chat.username}!')
@test_bot.message_handler(content_types=['text', 'audio', 'document', 'photo'])
def audio_text_doc_type(message):
    test_bot.reply_to(message,  f'Nice meme XDD, {message.chat.username}!')



test_bot.polling(none_stop=True)

