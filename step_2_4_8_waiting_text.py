from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip 
#from selenium.webdriver.support.ui import Select

try:
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))		
	
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
	WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), '$100')
		)
	# Нажать на кнопку "Забронировать"
	browser.find_element_by_id("book").click()

#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
	x = browser.find_element_by_id('input_value').text
	y = calc(int(x))
	ans = browser.find_element_by_id('answer')
	ans.send_keys(y)
# Нажать на кнопку "Submit".    
	browser.find_element_by_id("solve").click()

# В выскакивающем "alert" получаем строку-число и копируем в буфер обмена
	alert = browser.switch_to.alert
	alert_text = alert.text 
	alert_text = alert_text.split(': ')[-1]
	pyperclip.copy(alert_text)
#	alert.accept()
	print()
	print(alert_text)	

	
finally:
	# ждем 5 секунду
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла