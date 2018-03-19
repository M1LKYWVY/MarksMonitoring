try:
    from selenium import webdriver
except ImportError:
    print("Please check that selenium package installed through pip3 successfully")
    exit(1)


def check_de_ifmo(user):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1200x600W")
    driver = webdriver.Chrome("resources\\chromedriver.exe", chrome_options=options)
    driver.get("https://facebook.com")
    driver.get_screenshot_as_file("main-page.png")
