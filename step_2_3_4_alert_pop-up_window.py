from selenium import webdriver
import time
import math
import pyperclip 

#from selenium.webdriver.support.ui import Select

try:
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/alert_accept.html"
	browser.get(link)
# Нажать на кнопку
	button = browser.find_element_by_css_selector('button[type="submit"]')
	button.click()
# Принять confirm
	confirm = browser.switch_to.alert
	confirm.accept()
# На новой странице решить капчу для роботов, чтобы получить число с ответом
	x = browser.find_element_by_id('input_value').text
	y = calc(int(x))
	ans = browser.find_element_by_id('answer')
	ans.send_keys(y)
# Нажать на кнопку "Submit".    
	button = browser.find_element_by_tag_name("button")
	button.click()

# В выскакивающем "alert" получаем строку-число и копируем в буфер обмена
	alert = browser.switch_to.alert
	alert_text = alert.text 
	alert_text = alert_text.split(': ')[-1]
	pyperclip.copy(alert_text)
	alert.accept()
	print()
	print(alert_text)

finally:
	# ждем 5 секунду
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла