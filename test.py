from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://classroom.google.com/u/0/c/MTYxODI3NTY3Mjk0')
elem = driver.find_element_by_name('identifier')
time.sleep(1)
elem.send_keys('')
elem.send_keys(Keys.ENTER)
time.sleep(1)
psw = driver.find_element_by_name('password')
psw.send_keys('')
psw.send_keys(Keys.RETURN)
time.sleep(10)
driver.find_element_by_class_name("zTrXGf").click()
time.sleep(1)
post = driver.find_element_by_class_name('tL9Q4c')
post.send_keys('This post was made by an automation script')
driver.find_element_by_class_name('Fxmcu').click()
