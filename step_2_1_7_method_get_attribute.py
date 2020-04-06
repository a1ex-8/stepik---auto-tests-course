from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

# получаем значение атрибута "valuex" у картинки сундука
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    ans  = browser.find_element_by_id ('answer')
    ans.send_keys(y)
# выбираем Checkbox "I'm the robot" и нажимаем его
    Checkbox  = browser.find_element_by_css_selector('input#robotCheckbox')
    Checkbox.click()
# выбираем Radiobtton "Robots rule" и нажимаем его
    Radio = browser.find_element_by_id('robotsRule')
    Radio.click()   
    
# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    # ждем 4 секунду
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла