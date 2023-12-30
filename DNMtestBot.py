import telebot
from telebot import types
import webbrowser



bot = telebot.TeleBot('6567722769:AAHhE4_XROkMuW9PlfAKE9M-K1VbJvVpACg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://национальныепроекты.рф/map/detskiy-tekhnopark-kvantorium-kostromskoy-oblasti')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}!</b> Это пробный тестовый бот  \n Для помощи нажми /help',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help information</b>\n<em>Можно загружать изображения!\nУзнать свой ID > напиши id\nСайт моей работы > команда /site</em>',
                     parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url = 'https://translated.turbopages.org/proxy_u/en-ru.ru.34700b87-65647ddf-0e6cd51a-74722d776562/https/en.wikipedia.org/wiki/Image')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Какое красивое фото!', reply_markup = markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Какое некрасивое фото!', callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,
                         f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}!</b> Это пробный тестовый бот\n Для помощи нажми /help',
                         parse_mode='html')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'как дела?':
        bot.reply_to(message, f'Хорошо, {message.from_user.first_name}, надеюсь, у тебя тоже!')





bot.polling(none_stop=True)