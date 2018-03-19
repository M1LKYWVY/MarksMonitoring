from collections import namedtuple

from marks_monitoring import tg_bot
from marks_monitoring import student
import json
import threading


def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'User':
        return student.Student(obj["name"], obj["surname"], obj["user_name"], obj["password"])
    return obj


def main():
    # threading.Thread(target=lambda: tg_bot.bot.polling(none_stop=True)).start()
    # print("Telegram bot started successfully")
    x = student.Student("text", "text", "text", "text")
    z = json.dumps(x, default=lambda y: y.__dict__)
    f = json.loads(z, object_hook=lambda d: namedtuple("Student", d.keys())(*d.values()))
    print(type(f))


if __name__ == "__main__":
    main()
