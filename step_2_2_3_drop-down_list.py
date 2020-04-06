from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# 
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    x = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x)) 
    
# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ждем 4 секунду
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла