try:
    import telebot
except ImportError:
    print("Please check that telebot package was installed through \'pip\' successfully.")

import configparser

config = configparser.ConfigParser()
config.read("configs.ini")

bot = telebot.TeleBot(config["DEFAULT"]["Token"])

data = []


@bot.message_handler(content_types=["text"])
def on_update_received(message):
    print(message.text)
