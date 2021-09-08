from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element_by_css_selector('.first_block input.first[required]')
    input1.send_keys("First Name")
    
    input2 = browser.find_element_by_css_selector('.first_block input.second[required]')
    input2.send_keys("Last Name")

    input3 = browser.find_element_by_css_selector('.first_block input.third[required]')
    input3.send_keys("Email")        
            
    time.sleep(1)
    
    button = browser.find_element_by_tag_name('button')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text    

finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
