from time import sleep
import random
import telebot
import sqlite3
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

print("Бот https://t.me/xxxxxxxx ЗАПУЩЕН!!!")

bot = telebot.TeleBot('6359491544:AAHrw3OPo9Da7R-VUkgXrwVX5piputR6t6k')
name = None
user_id = 1


@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("itproger.sql")
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar('
                '50))')
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


lezt = ["Тебе подарили", "Ты поймал приступника и тебе дали", "Ты поработал на стройке‍ и получил",
        "Ты создал лекарство от рака и тебе дали за это", "Ты создал игру и заработал",
        "Ты продал тачку на аукционе и получил"]


@bot.message_handler(commands=['работать'])
def work_command(message):
    print("+1 пользователь")
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("работать")
    markup.add(btn1)


@bot.message_handler(content_types=['text'])
def work_command(message, points):
    if message.text == 'работать':
        ran_lezt = random.choice(lezt)
        ran = random.randint(1, 10)
        points += ran
        bot.send_message(message.chat.id, f"{ran_lezt} {ran}руб \n\nБаланс: {points}руб ")
        print(f"{message.from_user.first_name} наработал на {ran} золотых")
    elif message.text == 'SAN9N':
        command_sent = False
        if not command_sent:
            command_sent = True
            points += 1000
            bot.send_message(message.chat.id,
                             f"Ты успешно активировал промокод и получил 1000 рублей!!!\n\nТвой баланс: {points}руб ")
        else:
            bot.send_message(message.chat.id,
                             f"Ты уже активировал этот промокод!\n\nТвой баланс по-прежнему остается: {points}руб ")


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
    bot.send_message(message.chat.id, "Вот тебе меню", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text.lower() == "магазин":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("транспорт")
        item2 = types.KeyboardButton("одежда")
        back = types.KeyboardButton("назад")
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, "магазин", reply_markup=markup)

    elif message.text.lower() == "одежда":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("<<<предыдущее")
        item2 = types.KeyboardButton("следующее>>>")
        back = types.KeyboardButton("назад")
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, "магазин", reply_markup=markup)

    elif message.text.lower() == "транспорт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("<<<предыдущее.")
        item2 = types.KeyboardButton(".следующее>>>")
        back = types.KeyboardButton("назад")
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, "транспорт", reply_markup=markup)

    elif message.text.lower == "подарок":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("получить")
        back = types.KeyboardButton("назад")
        markup.add(item1, back)

        bot.send_message(message.chat.id, "подарок", reply_markup=markup)

    elif message.text.lower == "дом":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "это ваш дом")
        back = types.KeyboardButton("назад")
        markup.add(back)

        bot.send_message(message.chat.id, "дом", reply_markup=markup)

    elif message.text.lower == "не нажимать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "тебе сюда нельзя")
        back = types.KeyboardButton("назад")
        markup.add(back)

        bot.send_message(message.chat.id, "не нажимать", reply_markup=markup)

    elif message.text == "назад":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("работа")
        btn2 = types.KeyboardButton("магазин")
        btn3 = types.KeyboardButton("дом")
        markup.row(btn1, btn2, btn3)
        btn4 = types.KeyboardButton("статус")
        btn5 = types.KeyboardButton("подарок")
        btn6 = types.KeyboardButton("не нажимать")
        markup.row(btn4, btn5, btn6)
        bot.send_message(message.chat.id, "назад", reply_markup=markup)


bot.infinity_polling(none_stop=True)
