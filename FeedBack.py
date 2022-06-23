from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
link = "https://www.consult-info.ru/"
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(chrome_options=options)
browser.get(link)
text1 = browser.find_element_by_name("form_textarea_1")
text1.send_keys("Я хочу сайт по продаже кексиков")
text2 = browser.find_element_by_name("form_text_2")
text2.send_keys("Анастасия")
text3 = browser.find_element_by_name("form_text_3")
text3.send_keys("n.str@mail.ru")
directory ="C:/Users/neotm/Pictures/test"
file_name = "test.txt"
file_path = os.path.join(directory, file_name)
element = browser.find_element_by_class_name("inputfile")
element.send_keys(file_path)