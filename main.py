from marks_monitoring import tg_bot
import threading


def main():
    threading.Thread(target=lambda: tg_bot.bot.polling(none_stop=True)).start()
    print("Telegram bot started successfully")


if __name__ == "__main__":
    main()
