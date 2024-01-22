from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_link_text")

    number = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    link = browser.find_element(By.LINK_TEXT, number)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Nikita")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Dolgolenko")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Kostroma")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(7)
    browser.quit()