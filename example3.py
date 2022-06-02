
import telebot
from telebot import types
from telebot import callback_data
import random
import emoji

bot = telebot.TeleBot("НАДО ВСТАВИТЬ СВОЙ token")


# Функция для обработки последовательных inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == "example":
        msg = bot.send_message(call.message.chat.id, "А вот и третий пример 👉 /example3 ", reply_markup = markup)



# функция с нашим третьим примером
@bot.message_handler(commands=['example3'])
def example3(message):
    bot.send_message(message.chat.id, 'Вот тут мы отправляем текст')

    pic = open("privetexample.jpg", "rb")
    bot.send_photo(message.chat.id, pic)

    bot.send_contact(message.chat.id, phone_number=79998887766, first_name="Бот Анатолий", last_name="Прокат NFT великов за биткоин")

    sti = open("AnimatedStickerFrog.tgs", "rb")
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "✅ Двигаемся вперед 💪\n\nПопробуй модифицировать программу и дописать что-то свое, так лучше усвоится.\n\nrestart 👉 /example3")

#START функция с которой все начинается
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пример', callback_data='example')
    markup.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\nЛови первый пример из курса по разрабоке телеграм ботов *"PyTelegramBotAPI"*.\nПрисоединяйся к нам @JustDoItMotherBot'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


bot.polling(none_stop=True)
