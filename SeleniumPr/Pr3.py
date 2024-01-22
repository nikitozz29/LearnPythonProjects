from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    for element in elements:
        element.send_keys('Гениальный ответ')
    browser.find_element(By.XPATH, '//button').click()
    
   
finally:
    time.sleep(7)
    browser.quit()