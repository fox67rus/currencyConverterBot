import telebot

from settings import TOKEN
from extensions import currency, CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)


# Обработка команд
@bot.message_handler(commands=['start'])
def command_start(message: telebot.types.Message):
    text = f'Добрейшего времени суток вам, {message.chat.first_name}!\n\n' \
           'Для конвертирования валют отправьте боту сообщение в следующем формате:\n ' \
           '<имя валюты> <в какую валюту переводим> ' \
           '<количество переводимой валюты>\n' \
           'Например, чтобы узнать цену 100 долларов в рублях надо отправить сообщение: доллар рубль 100\n\n' \
           'Доступные команды: \n' \
           '- Введите /values, для получения списка доступных валют.\n' \
           '- Введите /about, для получения информации о боте.\n' \
           '- Введите /rate, для вывода текущего курса иностранных валют к рублю.\n' \
           '- Введите /help, для получения списка команд.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def command_help(message: telebot.types.Message):
    text = 'Для конвертирования валют отправьте боту сообщение в следующем формате:\n ' \
           '<имя валюты> <в какую валюту переводим> ' \
           '<количество переводимой валюты>\n' \
           'Например, чтобы узнать цену 100 долларов в рублях надо отправить сообщение: доллар рубль 100\n\n' \
           'Доступные команды: \n' \
           '- Введите /values, для получения списка доступных валют.\n' \
           '- Введите /about, для получения информации о боте.\n' \
           '- Введите /rate, для вывода текущего курса иностранных валют к рублю.\n' \
           '- Введите /help, для получения списка команд.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def command_values(message):
    text = 'Бот умеет работать со следующими валютами:'
    for key in currency.keys():
        text = '\n- '.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(commands=['about'])
def command_about(message):
    text = 'Бот написан в качестве контрольного проекта. \n Автор: Павлова Елена (QAP-1019)'
    bot.reply_to(message, text)


@bot.message_handler(commands=['rate'])
def command_rate(message):  # Дополнительная команда для получения курса валют
    usd_rate = CurrencyConverter.get_price('доллар', 'рубль', '1')
    eur_rate = CurrencyConverter.get_price('евро', 'рубль', '1')

    text = 'Курс валют к рублю на сегодня:\n' \
           f'1 USD = {usd_rate} RUB\n' \
           f'1 EUR = {eur_rate} RUB '

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().strip().split(' ')

        if len(values) != 3:
            raise APIException('Извините, я не понял, что вы хотите сделать.\n'
                               'Введите /help для вызова справки.')

        base, quote, amount = values
        if int(amount) <= 0:
            raise APIException('Количество переводимой валюты должно быть больше 0')

        total_base = CurrencyConverter.get_price(base, quote, amount)

    except APIException as user_error:
        bot.reply_to(message, f'Ошибка:\n{user_error}')
    except Exception as app_error:
        bot.reply_to(message, f'Хьюстон, у нас проблема:\n{app_error}')
    else:
        text = f'Конвертируем {base} в {quote}:\n' \
               f'Цена {amount} {currency[base]}  = {total_base} {currency[quote]}'
        bot.send_message(message.chat.id, text)


# дополнительные функции
# обработка других типов сообщений
@bot.message_handler(content_types=['photo', 'sticker'])
def repeat_photo_stick(message: telebot.types.Message):
    bot.reply_to(message, 'Красивая картинка! 😍\n Введите /help для вызова справки.')


@bot.message_handler(content_types=['voice', ])
def repeat_voice(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя красивый голос, но я ещё не умею распознать голосовые сообщения\n'
                                      'Введите /help для вызова справки.')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, 'Документы я пока не умею открывать.\n Введите /help для вызова справки.')


try:
    bot.polling(none_stop=True)
except ConnectionError as e:
    print('Ошибка подключения к боту:', e)
