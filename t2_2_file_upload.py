from selenium import webdriver
import time
import os

curr_dir = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(curr_dir, "file.txt")

#print(filename)

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("First Name")
    
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Last Name")

    input3 = browser.find_element_by_name('email')
    input3.send_keys("test@test.net")        

    input3 = browser.find_element_by_css_selector('input#file')
    input3.send_keys(filename)        
                
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)    

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
