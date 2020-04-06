from selenium import webdriver
#from selenium.webdriver.common.by import By 
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
#    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    x_element  = browser.find_element_by_id ('input_value')
    x = x_element.text
    y = calc(x)
    ans  = browser.find_element_by_id ('answer')
    ans.send_keys(y)
    Checkbox  = browser.find_element_by_css_selector('input#robotCheckbox')
    Checkbox.click()
    Radio = browser.find_element_by_id('robotsRule')
    Radio.click()    
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()