import configparser

from . import student, dbservice, scraper

try:
    import telebot
except ImportError(telebot):
    print("Please check that telebot package was installed through pip3 successfully.")

try:
    __config = configparser.ConfigParser()
    __config.read("configs.ini")
    bot = telebot.TeleBot(__config["BOT_INFO"]["Token"])
except KeyError:
    print("Check name of file with configs of telegram bot. "
          "It should be located near to package (.pyz) and named like \'configs.ini\'")
    exit(1)


@bot.message_handler(content_types=["text"], commands=["get_points"])
def get_condition(message):
    stu = dbservice.get_user(message.from_user.id)
    message_text = "Твои оценки за %d семестр:\n\n" % stu.active_semester
    dictionary = stu.points[0]
    for word in dictionary:
        message_text += "{!s}\t:\t{}\n".format(word, dictionary[word])
    bot.send_message(stu.tg_chat_id, message_text)


@bot.message_handler(content_types=["text"], commands=["change_semester"])
def change_semester(message):
    bot.send_message(message.from_user.id, "Feature in development")


@bot.message_handler(content_types=["text"], commands=["check_points"])
def check_condition(message):
    bot.send_message(message.from_user.id, "Проверка запущена, жди")
    is_pass_incorrect = scraper.check_de_ifmo(dbservice.get_user(message.from_user.id))
    print(is_pass_incorrect)
    if is_pass_incorrect:
        bot.send_message(message.from_user.id, "Проверь пароли, не надо тормози")
        return
    get_condition(message)


@bot.message_handler(content_types=["text"], commands=["register"])
def register(message):
    arr = message.text.split(" ")
    for el in arr:
        if el is None:
            bot.send_message(message.from_user.id, "ты чего, издеваешься, проверь пасы")
            return
    try:
        stu = dbservice.get_user(message.from_user.id)
        stu.password = arr[2]
        stu.login = arr[1]
    except KeyError:
        stu = student.Student(message.from_user.first_name, message.from_user.last_name, arr[1], arr[2], 4,
                              message.from_user.id)
        dbservice.save_user(stu.tg_chat_id, stu)
        bot.send_message(message.from_user.id, "Ты был зарегистрирован. Можешь юзать сервис.")


@bot.message_handler(content_types=["text"], commands=["start"])
def greeting(message):
    bot.send_message(message.from_user.id, "Приветствую!\n"
                                           "Я занимаюсь мониторингом ваших оценок!\n"
                                           "(если вы учитесь в итмо, конечно же).\n"
                                           "Итак, вам надо сказать мне, что мониторить.\n"
                                           "Регистрация несложная, нужно отправить такую штуку:\n"
                                           "login, password - логин и пасс для de.ifmo.ru\n"
                                           "/register login password\n"
                                           "Пример: /register 223619 lyblbyphp\n"
                                           "И да, если ошибся, продублируй команду /register с правильными пасами\n"
                                           "Только учти, что указать надо будет и логин, и пароль.")


@bot.message_handler(content_types=["text"])
def unrecognized_commands(message):
    bot.send_message(message.from_user.id, "Не могу понять, что ты хочешь от меня...\n"
                                           "Пиши, если что. @mentalinsanity ruslan.filichkin@iCloud.com")
