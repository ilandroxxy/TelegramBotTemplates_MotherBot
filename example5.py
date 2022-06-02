
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
        msg = bot.send_message(call.message.chat.id, "А вот и пятый пример 👉 /example5 ", reply_markup = markup)

    if call.data == "exitexample":
        msg = bot.send_message(call.message.chat.id, "Спасибо за просмотр, попробуй модифицировать программу и дописать что-то свое, так лучше усвоится.", reply_markup = markup)

# функция с нашим пятым примером
@bot.message_handler(commands=['example5'])
def example5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("A")
    btn2 = types.KeyboardButton("B")
    btn3 = types.KeyboardButton("C")
    btn4 = types.KeyboardButton("D")
    markup.add(btn1, btn2, btn3, btn4)
    question_messsage = 'В каком году было крещение Руси?\nA)  998\nB)  992\nC)  988\nD)  990'
    bot.send_message(message.chat.id, question_messsage , parse_mode="Markdown", reply_markup=markup)

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

    if get_message_bot == "A":
        bot.send_message(message.chat.id, "Ответ неверный")
    elif get_message_bot == "B":
        bot.send_message(message.chat.id, "Ты был близок")
    elif get_message_bot == "D":
        bot.send_message(message.chat.id, "Попытка не пытка...")
    elif get_message_bot == "C":
        bot.send_message(message.chat.id, "Верно, молодец!")
        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton("Телепорт 🔮", callback_data='exitexample'))
        bot.send_message(message.chat.id, "✨", reply_markup=markup3)

bot.polling(none_stop=True)