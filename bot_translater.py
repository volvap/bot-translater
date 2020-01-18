import re
import string
from telebot import TeleBot
from YandexTranslate import *
from googletrans import Translator

from db import *
from config import TOKEN
from config import KEY

bot = TeleBot(TOKEN)
key = KEY
db = Database()



@bot.message_handler(content_types=['text'])
def fallback(message):
    api = YTranslate(key)

    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

    translated_dict = api.translate(message.text,'ru')
    translated_word = str(list(translated_dict.values())[-1])

    temp = translated_word[2:]
    temp = temp[:-2]

    translated_google_word = translator.translate(message.text,dest='ru',src='en')
    bot.send_message(message.chat.id,f"GOOGLE :{translated_google_word.text.upper()}")
    bot.send_message(message.chat.id,f"YANDEX :{temp.upper()}")

if __name__ == '__main__':
    bot.polling()
