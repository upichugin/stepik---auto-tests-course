from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(1)

##    alert = browser.switch_to.alert
##    alert.accept()
##
##    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)    

    element1 = browser.find_element_by_css_selector("#input_value")
    num1 = element1.text
    secret_val = calc(num1)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(secret_val)
        
##    input2 = browser.find_element_by_css_selector("input#robotCheckbox")
##    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
##    input2.click()
##    
##    input3 = browser.find_element_by_css_selector("input#robotsRule")
##    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
##    input3.click()
    
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    
    time.sleep(10)
    
finally:
    browser.quit()    
