
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
        msg = bot.send_message(call.message.chat.id, "А вот и первый пример 👉 /example2 ", reply_markup = markup)

    if call.data == "exitexample":
        msg = bot.send_message(call.message.chat.id, "Спасибо за просмотр, попробуй модифицировать программу и дописать что-то свое, так лучше усвоится.", reply_markup = markup)

# функция с нашим вторым примером
@bot.message_handler(commands=['example2'])
def example2(message):
    markup = types.InlineKeyboardMarkup()
    bot.reply_to(message, 'Посчитаем факториал числа:\n(Не превышающего 1000) ')

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        x = message.text
        if x.isdigit() == True and 0 < int(x) <= 1000:
            temp = int(x)
            res = 1
            while temp > 0:
                res *= temp
                temp = temp - 1
            markup.add(types.InlineKeyboardButton("Закончить", callback_data='exitexample'))
            bot.send_message(message.chat.id, f'Факториал числа: {x} = {res}', reply_markup=markup)
        else:
            bot.reply_to(message, 'Я в такие игры не играю.. 👉 /example2 ')
    bot.register_next_step_handler(message, message_input)

#START функция с которой все начинается
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пример', callback_data='example')
    markup.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\nЛови первый пример из курса по разрабоке телеграм ботов *"PyTelegramBotAPI"*.\nПрисоединяйся к нам @JustDoItMotherBot'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


bot.polling(none_stop=True)