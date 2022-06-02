
import telebot
from telebot import types
from telebot import callback_data
import random
import emoji
from time import sleep

bot = telebot.TeleBot("НАДО ВСТАВИТЬ СВОЙ token")


# Функция для обработки последовательных inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == "example":
        msg = bot.send_message(call.message.chat.id, "А вот и шестой пример 👉 /example6 ", reply_markup = markup)


    elif call.data == 'exampleGameInlineButton':
        Step = ['Камень', 'Ножницы', 'Бумага', '1️⃣ Раз!', '2️⃣ Два!', '3️⃣ Три!']
        Massive = ['КАМЕНЬ', 'НОЖНИЦЫ', 'БУМАГА!']
        for i in range(0, len(Step)):
            msg = bot.send_message(call.message.chat.id, Step[i])
            sleep(0.6)

        x = random.randint(0, 2)
        msg = bot.send_message(call.message.chat.id, '▶️' + Massive[x])
        sleep(2)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🎮 Play", callback_data='exampleGameInlineButton'))
        msg = bot.send_message(call.message.chat.id, 'Давай сыграем снова!', parse_mode="Markdown", reply_markup=markup)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Back", callback_data='exitexample'))
        msg = bot.send_message(call.message.chat.id, 'Или продолжим учиться', parse_mode="Markdown", reply_markup=markup2)


    if call.data == "exitexample":
        msg = bot.send_message(call.message.chat.id, "Спасибо за просмотр, попробуй модифицировать программу и дописать что-то свое, так лучше усвоится.", reply_markup = markup)

# функция с нашим шестым примером
@bot.message_handler(commands=['example6'])
def example6(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎮 Play", callback_data='exampleGameInlineButton'))
    bot.send_message(message.chat.id, 'Сыграй с компьютером в игру:\n"Камень, ножницы, бумага"' , parse_mode="Markdown", reply_markup=markup)

#START функция с которой все начинается
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пример', callback_data='example')
    markup.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\nЛови первый пример из курса по разрабоке телеграм ботов *"PyTelegramBotAPI"*.\nПрисоединяйся к нам @JustDoItMotherBot'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)



bot.polling(none_stop=True)