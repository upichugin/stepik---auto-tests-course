from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser.get(link)

    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_tag_name("button")
    button.click()

    #time.sleep(1)

    element1 = browser.find_element_by_css_selector("#input_value")
    num1 = element1.text
    secret_val = calc(num1)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(secret_val)
    
    button = browser.find_element_by_css_selector("#solve")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    
    time.sleep(10)
    
finally:
    browser.quit()    
