import os
from dotenv import load_dotenv
import telebot

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

user_login = {}
user_password = {}


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}, я бот, который выполнит вашу авторизацию.'
                     '\nФункции моей работы:'
                     '\n1) /authorization - выполняет вашу авторизацию.')


@bot.message_handler(commands=['authorization'])
def start_authorization(message):
    bot.send_message(message.chat.id, "Введите ваш логин:")
    bot.register_next_step_handler(message, process_login_step)


def process_login_step(message):
    user_login[message.chat.id] = message.text
    bot.send_message(message.chat.id, "Введите ваш пароль:")
    bot.register_next_step_handler(message, process_password_step)


def process_password_step(message):
    user_password[message.chat.id] = message.text
    login = os.getenv("APP_LOGIN")
    password = os.getenv("APP_PASSWORD")

    if login == user_login[message.chat.id] and password == user_password[message.chat.id]:
        bot.send_message(message.chat.id, "Вы успешно авторизовались!")
    else:
        bot.send_message(message.chat.id, "Неверный логин или пароль.")


bot.polling(none_stop=True)