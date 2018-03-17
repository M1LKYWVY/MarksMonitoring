try:
    import telebot
except ImportError:
    print("Please check that telebot package was installed through \'pip\' successfully.")

from . import configs

data = []

bot = telebot.TeleBot(configs.token)
