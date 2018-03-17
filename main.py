from marks_monitoring import tg_bot
from marks_monitoring import writer

try:
    from selenium import webdriver
except ImportError:
    print("Please check that selenium package was installed through \'pip\' successfully.")


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1200x600W")
    driver = webdriver.Chrome("resources\\chromedriver.exe", chrome_options=options)
    driver.get("https://facebook.com")
    driver.get_screenshot_as_file("main-page.png")


if __name__ == "__main__":
    tg_bot.bot.polling(non_stop=True)
    tg_bot.data = writer.read("")
    # TODO change file
    main()
