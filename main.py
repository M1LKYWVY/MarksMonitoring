from marks_monitoring import tg_bot
from marks_monitoring import writer
import sys

try:
    from selenium import webdriver
except ImportError:
    print("Please check that selenium package was installed through \'pip\' successfully.")


def main():
    if len(sys.argv) == 1:
        print("Please check path to file data.json")
        return
    file = open(sys.argv[1], mode="r")
    tg_bot.data = writer.read(file)
    tg_bot.bot.polling(non_stop=True)
    # TODO change file


if __name__ == "__main__":
    main()
