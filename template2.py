import sqlite3
import telebot
from telebot import types
from telebot import callback_data
import random
import emoji
import time

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪
bot = telebot.TeleBot('ВАШ token')


# TEMPLATE1 - Запись клиента
def date_today(week):
    w = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    day = time.strftime('%d')
    month = time.strftime('%m')
    d = int(time.strftime('%w'))
    week.append(w[d] + '  ' + day + '.' + month)
    d += 1

    count = 1
    while d < 6:
        day = str(int(day) + 1)
        if int(day) == 31:
            day = '1'
            month = str(int(month) + 1)
        week.append(w[d] + '  ' + day + '.' + month)
        d += 1
        count += 1
        if count == 6:
            break
    d = 0
    while d < 6 and count < 6:
        day = str(int(day) + 1)
        if int(day) == 31:
            day = '1'
            month = str(int(month) + 1)
        week.append(w[d] + '  ' + day + '.' + month)
        d += 1
        count += 1
        if count == 6:
            break



    print(week)


    return week


#START при старте я создаю шесть inline кнопок начиная с сегодняшнего дня,
# формат вывода даты на кнопках я высчитываю через функцию date_today
@bot.message_handler(commands=['start'])
def start(message):
    week = []
    week = date_today(week)

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(week[0], callback_data="today"),
               types.InlineKeyboardButton(week[1], callback_data="second"),
               types.InlineKeyboardButton(week[2], callback_data="third"),
               types.InlineKeyboardButton(week[3], callback_data="fourth"),
               types.InlineKeyboardButton(week[4], callback_data="fifth"),
               types.InlineKeyboardButton(week[5], callback_data="sixth"))
    send_mess = "Выберите день для записи и списка: "
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


# Функция для обработки последовательных inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=4)

    # если выбор пал на сегодня, то я указываю свой рабочий график и обрабатываю кажду клавишу через событие
    if call.data == 'today':
        markup.add(types.InlineKeyboardButton('10:00', callback_data="today1"),
                   types.InlineKeyboardButton('11:00', callback_data="today2"),
                   types.InlineKeyboardButton('12:00', callback_data="today3"),
                   types.InlineKeyboardButton('13:00', callback_data="today4"),
                   types.InlineKeyboardButton('14:00', callback_data="today5"),
                   types.InlineKeyboardButton('15:00', callback_data="today6"),
                   types.InlineKeyboardButton('16:00', callback_data="today7"),
                   types.InlineKeyboardButton('17:00', callback_data="today8"))
        msg = bot.send_message(call.message.chat.id, "Какое вам будет удобно время?", parse_mode="Markdown", reply_markup=markup)

    # здесь я указываю смвой пользователя, чтобы получать уведомления о записях и отправляю user (id) в формате ссылки, чтобы можно было связаться с записавшимся

    # !!!! вместо 438879394 должен быть id вашего аккаунта, куда хотите получать уведомления
    elif call.data == 'today1':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 10:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today2':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 11:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today3':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 12:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today4':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 13:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today5':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 14:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today6':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 15:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today7':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 16:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'today8':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 17:00 {time.strftime('%d') +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")

    # все отсальные действия повторяются
    if call.data == 'second':
        markup.add(types.InlineKeyboardButton('10:00', callback_data="second1"),
                   types.InlineKeyboardButton('11:00', callback_data="second2"),
                   types.InlineKeyboardButton('12:00', callback_data="second3"),
                   types.InlineKeyboardButton('13:00', callback_data="second4"),
                   types.InlineKeyboardButton('14:00', callback_data="second5"),
                   types.InlineKeyboardButton('15:00', callback_data="second6"),
                   types.InlineKeyboardButton('16:00', callback_data="second7"),
                   types.InlineKeyboardButton('17:00', callback_data="second8"))
        msg = bot.send_message(call.message.chat.id, "Какое вам будет удобно время?", parse_mode="Markdown", reply_markup=markup)

    elif call.data == 'second1':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 10:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second2':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 11:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second3':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 12:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second4':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 13:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second5':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 14:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second6':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 15:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second7':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 16:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")
    elif call.data == 'second8':
        user = str(call.message.chat.id)
        msg = bot.send_message(438879394, f"tg://user?id={user} запись на 17:00 {str(int(time.strftime('%d'))+1) +'.'+time.strftime('%m')}")
        msg = bot.send_message(call.message.chat.id, "Дата выбрано, свяжусь с вам в ближайшее время!")


# Масштобировать пример я не буду, действия повторяются, только в {str(int(time.strftime('%d'))+1) надо делать +2, +3 и т.д.
    if call.data == 'third':
        pass

    if call.data == 'fourth':
        pass

    if call.data == 'fifth':
        pass

    if call.data == 'sixth':
        pass


bot.polling(none_stop=True)