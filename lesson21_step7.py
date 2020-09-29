import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    print('x=', x)
    y = calc(x)

    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
