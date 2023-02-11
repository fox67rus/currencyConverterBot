import telebot

import settings
from extensions import currency, CurrencyConverter, APIException

TOKEN = settings.TOKEN
bot = telebot.TeleBot(TOKEN)


# Обработка команд
@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    print(message.text)
    text = 'Для начала работы введите команду боту в следующем формате:\n ' \
           '<имя валюты> <в какую валюту переводим> ' \
           '<количество переводимой валюты>\n' \
           'Например, доллар рубль 100\n\n' \
           'Введите /values, для получения списка доступных валют.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def handle_start_help(message):
    print(message.text)
    text = 'Бот умеет работать со следующими валютами:'
    for key in currency.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    print(message.text)
    values = message.text.split(' ')  # доллар рубль 1

    if len(values) != 3:
        raise APIException('Неправильный формат команды.')

    quote, base, amount = values
    total_base = CurrencyConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


# обработка других типов сообщений
@bot.message_handler(content_types=['photo', 'sticker'])
def repeat_photo_stick(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, 'Красивая картинка! 😍')


@bot.message_handler(content_types=['voice', ])
def repeat_voice(message: telebot.types.Message):
    print(message.text)
    bot.send_message(message.chat.id, 'У тебя красивый голос, но я ещё не умею распознать голосовые сообщения')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    print(message.text)
    bot.reply_to(message, 'Документы я пока не умею открывать')


bot.polling(none_stop=True)
