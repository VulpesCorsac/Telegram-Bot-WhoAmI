import telebot

from secrets import Secrets

bot = telebot.TeleBot(Secrets['bot_api_token'])

bot.set_my_name('WhoAmI')
bot.set_my_short_description('This bot will send you back your telegram information')
bot.set_my_description('This bot will send you back your telegram information: id, name, surname, language, premium...')
bot.set_my_commands([
    telebot.types.BotCommand('/start', 'Greet user with his id or hardcoded name'),
    telebot.types.BotCommand('/who_am_i', 'Print user information'),
])


@bot.message_handler(commands=['start'])
def work(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')


@bot.message_handler(commands=['who_am_i'])
def get_info(message):
    reply = f'Username: @{message.from_user.username}\n' \
            f'Id: {message.from_user.id}\n' \
            f'First name: {message.from_user.first_name}\n' \
            f'Last name: {message.from_user.last_name}\n' \
            f'Bot: {message.from_user.is_bot}\n' \
            f'Language code: {message.from_user.language_code}\n' \
            f'Premium user: {message.from_user.is_premium}\n'
    bot.send_message(message.chat.id, reply)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.infinity_polling()
