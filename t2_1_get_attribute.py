from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_css_selector("img#treasure")
    value_x = element.get_attribute("valuex")
    secret_val = calc(value_x)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(secret_val)
        
    input2 = browser.find_element_by_css_selector("input#robotCheckbox")
    input2.click()
    
    input3 = browser.find_element_by_css_selector("input#robotsRule")
    input3.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)    

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
