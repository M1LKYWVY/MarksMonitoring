from datetime import datetime
from collections import namedtuple

from marks_monitoring import tg_bot
from marks_monitoring import student
from marks_monitoring import scraper
from marks_monitoring import dbservice
import json
import threading


def main():
    threading.Thread(target=lambda: tg_bot.bot.polling(none_stop=True)).start()
    print("Telegram bot started successfully")


if __name__ == "__main__":
    main()
