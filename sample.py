from selenium import webdriver


link = ""
browser = webdriver.Chrome()
try:
    browser.get(link)

finally:
    # успеваем скопировать код за 30 секунд
    # закрываем браузер после всех манипуляций
    browser.quit()
