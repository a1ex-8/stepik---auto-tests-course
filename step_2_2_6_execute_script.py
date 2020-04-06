from selenium import webdriver
import time
import math
#from selenium.webdriver.support.ui import Select

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
# Считать значение для переменной x. Посчитать математическую функцию от x.
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
#Ввести ответ в текстовое поле.
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
# Выбрать checkbox "I'm the robot". Переключить radiobutton "Robots rule!".
# Проскроллить страницу вниз.
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()
# Нажать на кнопку "Submit".    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ждем 5 секунду
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла