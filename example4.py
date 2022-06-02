
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
        msg = bot.send_message(call.message.chat.id, "А вот и четвертый пример 👉 /example4 ", reply_markup = markup)

    if call.data == "exitexample":
        msg = bot.send_message(call.message.chat.id, "Спасибо за просмотр, попробуй модифицировать программу и дописать что-то свое, так лучше усвоится.", reply_markup = markup)

# функция с нашим четвертым примером
@bot.message_handler(commands=['example4'])
def example4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Круто")
    btn2 = types.KeyboardButton("Не очень, я устал")
    btn3 = types.KeyboardButton("Как вернуться назад?")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Скажи мне, как у тебя дела?', parse_mode="Markdown", reply_markup=markup)

#START функция с которой все начинается
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пример', callback_data='example')
    markup.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\nЛови первый пример из курса по разрабоке телеграм ботов *"PyTelegramBotAPI"*.\nПрисоединяйся к нам @JustDoItMotherBot'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

# функция обработки введенного текста от пользователя
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Круто":
        bot.send_message(message.chat.id, "Молодец, так держать 💪")

    elif get_message_bot == "Не очень, я устал":
        bot.send_message(message.chat.id, "Сделай паузу, продолжишь завтра!")

    elif get_message_bot == "Как вернуться назад?":

        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton("Телепорт 🔮", callback_data='exitexample'))
        bot.send_message(message.chat.id, "✨", reply_markup=markup3)

bot.polling(none_stop=True)