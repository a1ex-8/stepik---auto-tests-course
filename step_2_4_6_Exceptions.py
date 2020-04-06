from selenium import webdriver
import time
import math
import pyperclip 

#from selenium.webdriver.support.ui import Select

try:
	browser = webdriver.Chrome()
	# говорим WebDriver искать каждый элемент в течение 5 секунд
	browser.implicitly_wait(5)

	browser.get("http://suninjuly.github.io/cats.html")

	browser.find_element_by_id("button")

finally:
	# ждем 5 секунду
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла