from selenium import webdriver
import time
import os 

#from selenium.webdriver.support.ui import Select

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)
# Заполнить текстовые поля: имя, фамилия, email
	parametrs = browser.find_elements_by_css_selector('[type="text"]')
	for parametr in parametrs:
		parametr.send_keys("FIO")
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
	InputFile = browser.find_element_by_css_selector('input[type="file"]')
	InputFile.send_keys(file_path)
# Нажать на кнопку "Submit".    
	button = browser.find_element_by_tag_name("button")
	button.click()

finally:
	# ждем 5 секунду
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла