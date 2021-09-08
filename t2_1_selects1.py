from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x1,x2):
  return str(int(x1)+int(x2))

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("#num1")
    num1 = element1.text
    element2 = browser.find_element_by_css_selector("#num2")
    num2 = element2.text
    
    secret_val = calc(num1, num2)

    select = Select(browser.find_element_by_css_selector("select#dropdown"))
    select.select_by_visible_text(secret_val)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)    

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
