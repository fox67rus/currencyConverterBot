import telebot

from settings import TOKEN
from extensions import currency, CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)


# Обработка команд
@bot.message_handler(commands=['start', 'help'])
def command_start_help(message: telebot.types.Message):
    print(message.text)
    text = 'Для начала работы введите команду боту в следующем формате:\n ' \
           '<имя валюты> <в какую валюту переводим> ' \
           '<количество переводимой валюты>\n' \
           'Например, доллар рубль 100\n\n' \
           'Введите /values, для получения списка доступных валют.\n' \
           'Введите /about, для получения информации о боте.\n' \
           'Введите /help, для получения списка команд.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def command_values(message):
    print(message.text)
    text = 'Бот умеет работать со следующими валютами:'
    for key in currency.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(commands=['about'])
def command_about(message):
    print(message.text)
    text = 'Бот написан в качестве контрольного проекта. \n Автор: Павлова Елена (QAP-1019)'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    print(message.text)

    try:
        values = message.text.split(' ')  # доллар рубль 1

        if len(values) != 3:
            raise APIException('Неправильный формат команды. Введите /help для вызова справки.')

        base, quote, amount = values
        total_base = CurrencyConverter.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка:\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Хьюстон, у нас проблема:\n{e}')
    else:
        text = f'Конвертируем {base} в {quote}:\n' \
               f'Цена {amount} {currency[base]}  = {total_base} {currency[quote]}'
        bot.send_message(message.chat.id, text)


# обработка других типов сообщений
@bot.message_handler(content_types=['photo', 'sticker'])
def repeat_photo_stick(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, 'Красивая картинка! 😍\n Введите /help для вызова справки.')


@bot.message_handler(content_types=['voice', ])
def repeat_voice(message: telebot.types.Message):
    print(message.text)
    bot.send_message(message.chat.id, 'У тебя красивый голос, но я ещё не умею распознать голосовые сообщения\n'
                                      'Введите /help для вызова справки.')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    print(message.text)
    bot.reply_to(message, 'Документы я пока не умею открывать.\n Введите /help для вызова справки.')


bot.polling(none_stop=True)
