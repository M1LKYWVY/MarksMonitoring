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
        exit(1)
    driver.get("https://de.ifmo.ru/?node=signin")
    driver.implicitly_wait(10)
    driver.find_element_by_id("login").send_keys(student.user_name)
    driver.find_element_by_id("password").send_keys(student.password)
    driver.find_element_by_css_selector(".signin > input:nth-child(7)").click()
    driver.find_element_by_css_selector("#d_s_m_menu > ul:nth-child(13) > li:nth-child(1) > a:nth-child(1)").click()
    driver.get_screenshot_as_file("main-page.png")
    table_rows = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1)")\
        .find_elements_by_tag_name("tr")
    skip_rows = True
    dictionary = {}
    for row in table_rows:
        if "Семестр" in row.text:
            if str(student.active_semester) in row.text:
                skip_rows = False
                continue
            if str(student.active_semester) not in row.text and not skip_rows:
                skip_rows = True
                continue
        if skip_rows:
            continue

        cells = row.find_elements_by_tag_name("td")
        value = cells[3].text.replace(",", ".")
        if value == "":
            value = "0"
        dictionary[cells[2].text] = float(value)
        # student.points.insert(student.active_semester-1, {cells[2]: cells[3]})
        # student.points[student.active_semester-1][cells[2]] = cells[3]
        # print(row.text)
        # cells = row.find_elements_by_tag_name("td")
        # print(len(cells))
        # if "Семестр" in row.text:
        #     continue
        # print(row.find_elements_by_tag_name("td")[2].text, row.find_elements_by_tag_name("td")[3].text)
    # for i in range(3, 30):
    #     x = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
    #                                             "> tr:nth-child(" + str(i) + ")")
    #     value = x.find_element_by_css_selector("td:nth-child(" + str(4) + ")").text.replace(",", ".")
    #
    #     print(value)
    #     if len(str(x.text)) <= 12 or value == "":
    #         print(x.text == "Семестр 4")
    #         continue
    #
    #     print(value)
    #     student.points[0][x.find_element_by_css_selector("td:nth-child(" + str(3) + ")").text] \
    #         = float(str(value))
        # q = x.find_element_by_css_selector("td:nth-child(" + str(4) + ")")
        # f = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
        #                                         "> tr:nth-child(3) > td:nth-child(4)")
        # g = driver.find_element_by_css_selector("div.d_text:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) "
        #                                         "> tr:nth-child(4)")
    # for var in dictionary:
    #     print(var, " ", dictionary[var])
    # for var in student.points[3]:
    #     print(var)
    student.points.insert(student.active_semester-1, dictionary)
    driver.close()
    return student
