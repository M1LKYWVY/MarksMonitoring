from datetime import datetime
from collections import namedtuple

from marks_monitoring import tg_bot
from marks_monitoring import student
from marks_monitoring import scraper
from marks_monitoring import dbservice
import json
import threading


def main():
    # threading.Thread(target=lambda: tg_bot.bot.polling(none_stop=True)).start()
    # print("Telegram bot started successfully")
    # print(datetime.now().strftime("%m"))
    # TODO USE date to check semester
    scraper.check_de_ifmo(student.Student("Руслан", "Филичкин", "223619", "papamama1975", 4, 63312273))
    # dbservice.get_user(student.Student("Руслан", "Филичкин", "223619", "papamama1975", 4, 63312273))


if __name__ == "__main__":
    main()
