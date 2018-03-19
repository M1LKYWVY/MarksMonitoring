import configparser

try:
    import telebot
except ImportError:
    print("Please check that telebot package was installed through pip3 successfully.")

try:
    __config = configparser.ConfigParser()
    __config.read("configs.ini")
    bot = telebot.TeleBot(__config["BOT_INFO"]["Token"])
except KeyError:
    print("Check name of file with configs of telegram bot. "
          "It should be located near to package (.pyz) and named like \'configs.ini\'")
    exit(1)


@bot.message_handler(content_types=["text"], commands=["get_condition"])
def get_condition(message):
    print("qq" + message.text)


@bot.message_handler(content_types=["text"], commands=["change_semester"])
def change_semester(message):
    print("qqq" + message.text)


@bot.message_handler(content_types=["text"], commands=["check_condition"])
def check_condition(message):
    print("qqqq" + message.text)


@bot.message_handler(content_types=["text"], commands=["start"])
def greeting(message):
    pass


@bot.message_handler(content_types=["text"])
def unrecognized_commands(message):
    print("q" + message.text)
