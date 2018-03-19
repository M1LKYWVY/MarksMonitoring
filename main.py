from marks_monitoring import tg_bot


def main():
    tg_bot.bot.polling(none_stop=True)
    print("Telegram bot started successfully")


if __name__ == "__main__":
    main()
