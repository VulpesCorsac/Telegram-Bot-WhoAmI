import telebot

from secrets import Secrets

bot = telebot.TeleBot(Secrets['bot_api_token'])

bot.remove_webhook()
bot.set_webhook(Secrets['api_gateway'])
