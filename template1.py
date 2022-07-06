import telebot  # билиотека для корректной работы PyTelegramBotAPI
from telebot import types
from telebot import callback_data

import emoji  # библиотека, чтобы работали эмоджи

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯
bot = telebot.TeleBot('ТвойToken')
# Подробнее читайте в разделе "Что такое token?"



@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # Блок 1 -----------------------------------------------------------------------
    if call.data == 'price':

        pic_2 = open("ТвойФайлКартинкиПрайсаВЛюбомРазрешении.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_2)
        # Подробнее можно прочитать в разделе "Бот отправляет"

        send_message2 = f"Тут мы напишем какой-то сопроводительный текст для Прайса\n\n" \
                        f"\nЭтот значок позволяет разделить текст пустой строкой\n\n" \
                        f"*А эти звездочки соответсвуют разметки Markdown - жирный шрифт*\n\n" \
                        f"_Курсив_\n\n"

        markup = types.InlineKeyboardMarkup(row_width=1)  #указываем кол-во кнопок в строке, в данном случае одно слово на строку
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"), # по ключам callback_data="ключ" мы обращаемся к структурам описанным и вызываемым из:
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"))    # @bot.callback_query_handler(func=lambda call: True)

        # Хочу обратить внимание, что в функции callback_query любые действия бота сопровождаются msg =
        # и вместо message.chat.id нужно писать call.message.chat.id
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown", reply_markup=markup)

        # parse_mode="Markdown" подключает разметку Markdown, еще есть вариант HTML
        # reply_markup=markup - отображает кнопки созданные на строчке 27-30

    elif call.data == "iam":
        send_message1 = f"Тут пишем текст о себе"
        msg = bot.send_message(call.message.chat.id, send_message1, parse_mode="Markdown")

        # Захотел сделать кнопку с ссылкой на отзывы
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton("Отзывы", url = 'https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing'))

        pic_3 = open("ТвойФайлКартинкаАватарка.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_3, reply_markup=markup1)
        # При отправки картинки, отобразил кнопки markup1

        # Создали еще кнопки, но уже в другом markup2, чтобы отобразить в другом месте (в другое время работы бота)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        send_message2 = f"К сожалению мы не можем отобразить кнопки без какого-либо объекта: текст, фото, войс... "
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown")



    elif call.data == "download":
        # В целом никто не запрещает на отправлять ссылки без кнопок, работать будут так же
        send_message = f"*Ссылки для скачивания программ:*\n\n" \
                       f"Python https://www.python.org/downloads/\n\n" \
                       f"Pycharm https://www.jetbrains.com/ru-ru/pycharm/download/#section=mac\n\n" \
                       f"Discord https://discord.com/download\n\n" \
                       f"Telegram Desktop https://telegram.org/"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)
    # Блок 1 -----------------------------------------------------------------------



# команда START запускает бота, по сути говоря, приветствуем бота
@bot.message_handler(commands=['start'])
def start(message):

    # Тут мы используем стандартную клавиатуру, которая замещает ввод текста пользователем
    # Подробная информация в разделе "KeyboardButton"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # 3 кнопки в строке
    btn1 = types.KeyboardButton('Контакты')
    btn2 = types.KeyboardButton('Репетитор')
    btn3 = types.KeyboardButton('Мои проекты')
    btn4 = types.KeyboardButton('Создать бота под заказ')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\n'

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

# HELP
@bot.message_handler(commands=['help'])
def help(message):
    send_message = "\n\nI can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual.\n\n" \
                   "You can control me by sending these commands:\n\n*Commands*\n/help - навигация по командам\n/start - перезапустить бота\n" \
                   '/myproject - список моих актуальных проектов'
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")

# MYPROJECT
# Про команды подробнее читайте в "Команды и функции"
@bot.message_handler(commands=['myproject'])
def myproject(message):
    send_message = "Не стану перечислять провальные проекты, просто перечислю, чем я занимаюсь сегодня!\n\n" \
                   "*1. itpy | ИнформатикаЕГЭ*\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                   "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе. \nА это для будущих программистов - куда важнее экзаменов.\n\n" \
                   "*2. @MotherBot*\n🤖 Это Telegram бот, который помогает начинающим программистам разобраться в библиотеке PyTelegramBotAPI, предназначенной " \
                   "для работы с API Telegram - создания Ботов в меcсенджере. \nКурс рассчитан на поверхностные знания языка Python, без возрастных ограничений.\n"

    # А это клавиатура inline клавиш, они могут выполнять цепочки событий через callback_data, но с текстом никак не связаны
    # Подробная информация в разделе "InlineButton"
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Канал подготовки к ЕГЭ по Информатике", url="https://t.me/pro100_easy_ege"),
               types.InlineKeyboardButton("@MotherBot курс по разработке ботов", url="https://t.me/JustDoItMotherBot"))  # например здесь используется событие - переход по ссылке

    bot.send_message(message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)

# Это специальная функция, которая помогает обрабатывать текст и ReplayKeyboardButton
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()  # возвращаем и обрабатываем копию строки введенную пользователем

    if get_message_bot == "Репетитор":
        markup0 = types.InlineKeyboardMarkup(row_width=1)
        markup0.add(types.InlineKeyboardButton("Канал: itpy | ИнформатикаЕГЭ", url='https://t.me/pro100_easy_ege'))

        send_message1 = f"Я работаю дистанционно.."

        bot.send_message(message.chat.id, send_message1, parse_mode="Markdown", reply_markup=markup0)


        pic_4 = open("ФайлыМожноИспользоватьВЛюбюбомФормате.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_4)


        send_message4 = f"Здесь я открываю меню inline кнопок, которое затем обрабатывается в функции: @bot.callback_query_handler(func=lambda call: True) - строка 12"
        # Подробная информация в разделе "InlineButton"
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))
        bot.send_message(message.chat.id, send_message4, parse_mode="Markdown", reply_markup=markup2)

    if get_message_bot == "Контакты":
        send_message1 = "*Мои контакты:*"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Профиль Авито", url='https://www.avito.ru/user/'))
        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', reply_markup=markup)

    if get_message_bot == "Мои проекты":
        send_message = "По сути, у меня есть функция /myproject которая полностью дублирует это действие, описание аналогичное - строка 105"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Канал подготовки к ЕГЭ по Информатике", url="https://t.me/pro100_easy_ege"),
                   types.InlineKeyboardButton("@MotherBot курс по разработке ботов", url="https://t.me/JustDoItMotherBot"))
        bot.send_message(message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)



    if get_message_bot == "Создать бота под заказ":

        send_message0 = "Здесь я собираю заявки на создание, специальная функция - строка 170 обрабатывает текст и отправляет его по моему id пользователя"
        bot.send_message(message.chat.id, send_message0, parse_mode='Markdown')


        @bot.message_handler(content_types=['text'])  # захватили сообщение, которое оставил пользователь
        def message_input(message):
            user_id = message.chat.id  # получили id пользователя, кто писал
            user_name = message.from_user.username  # получили, его @username


            text_message = "Пришла новая заявка на создание бота: \n*user:* @" + user_name + "\n\n_Письмо:_\n" + message.text
            bot.send_message(438879394, text_message, parse_mode='Markdown') # это сообщение улетает мне, как администратору

            bot.send_message(message.chat.id, "❗Заявка улетела ко мне (@ilandroxxy), постараюсь связаться с Вами в ближайшее время 🙏")
            # А это сообщение увидит пользователь, при успешной отправки сообщения

        bot.register_next_step_handler(message, message_input)


bot.polling(none_stop=True)  # позволяет держать постоянную связь запросов с сервером (без нее работать не будет)

