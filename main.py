import telebot
import json
import settings
import extensions

TOKEN = settings.TOKEN

bot = telebot.TeleBot(TOKEN)


# Обработка команд
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(message.text)
    bot.reply_to(message, f'Привет, {message.chat.first_name}! Это бот-конвертер.')


@bot.message_handler(content_types=['text', ])
def repeat_text(message: telebot.types.Message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['photo', 'sticker'])
def repeat_photo_stick(message: telebot.types.Message):
    bot.reply_to(message, 'Красивая картинка! 😍')


@bot.message_handler(content_types=['voice', ])
def repeat_voice(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя красивый голос, но я ещё не умею распознать голосовые сообщения')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, 'Документы я пока не умею открывать')


bot.polling(none_stop=True)
