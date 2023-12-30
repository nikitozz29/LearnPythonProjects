import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6359491544:AAHrw3OPo9Da7R-VUkgXrwVX5piputR6t6k')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'привет я бот багет создай себе имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'создай себе пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'ты зареган', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


@bot.message_handler(commands=["menu"])
def menu(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("работа")
    btn2 = types.KeyboardButton("магазин")
    btn3 = types.KeyboardButton("дом")
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton("статус")
    btn5 = types.KeyboardButton("подарок")
    btn6 = types.KeyboardButton("не нажимать")
    markup.row(btn4, btn5, btn6)
    bot.send_message(message.chat.id, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text == "магазин":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("транспорт")
        item2 = types.KeyboardButton("одежда")
        back = types.KeyboardButton("назад")
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, "магазин", reply_markup=markup)

    elif message.text == "подарок":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("получить")
        back = types.KeyboardButton("назад")
        markup.add(item1, back)

        bot.send_message(message.chat.id, "подарок", reply_markup=markup)

    elif message.text == "дом":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "это ваш дом: zaxpqr3erfsy4rzu4gkr5mmoi3lvj4f5.jpg")
        back = types.KeyboardButton("назад")
        markup.add(back)

        bot.send_message(message.chat.id, "дом", reply_markup=markup)


bot.infinity_polling(none_stop=True)
