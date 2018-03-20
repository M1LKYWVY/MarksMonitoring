import configparser

try:
    from selenium import webdriver, common
except ImportError(webdriver):
    print("Please check that selenium package installed through pip3 successfully")
    exit(1)

try:
    __config = configparser.ConfigParser()
    __config.read("configs.ini")
    path = __config["WEB_DRIVER_INFO"]["Location"]
except KeyError:
    print("Check name of file with configs of telegram bot. "
          "It should be located near to package (.pyz) and named like \'configs.ini\'")
    exit(1)


def check_de_ifmo(student):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1200x600W")
    try:
        driver = webdriver.Chrome(path, chrome_options=options)

    except common.exceptions.WebDriverException:
        print("Check path to executable chromedriver. Configs.ini stores path in [WEB_DRIVER_INFO] section as"
              " \'Location\'")
    driver.get("https://de.ifmo.ru/?node=signin")
    driver.implicitly_wait(10)
    driver.find_element_by_id("login").send_keys(student.user_name)
    driver.find_element_by_id("password").send_keys(student.password)
    driver.find_element_by_css_selector(".signin > input:nth-child(7)").click()
    driver.find_element_by_css_selector("#d_s_m_menu > ul:nth-child(13) > li:nth-child(1) > a:nth-child(1)").click()
    driver.get_screenshot_as_file("main-page.png")
    skip_rows = True
    for i in range(3, 30):
        x = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
                                                "> tr:nth-child(" + str(i) + ")")
        if len(str(x.text)) <= 12:
            print(x.text == "Семестр 4")
            continue
        q = x.find_element_by_css_selector("td:nth-child(" + str(3) + ")")
        q = x.find_element_by_css_selector("td:nth-child(" + str(4) + ")")
        # f = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
        #                                         "> tr:nth-child(3) > td:nth-child(4)")
        # g = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
        #                                         "> tr:nth-child(4)")
    driver.close()
