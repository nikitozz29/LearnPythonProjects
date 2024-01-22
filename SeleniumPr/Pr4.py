from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Nikita")
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Dolgolenko")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("Kostroma")
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//div[6]/button[3]")
    button.click()
    
   
finally:
    time.sleep(7)
    browser.quit()