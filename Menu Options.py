from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/Users/fxrxbx/Downloads/chromedriver')

driver.get("https://qa-challenge.codesubmit.io/")

element = driver.find_element(By.ID, "user-name")
element.clear()
element.send_keys("standard_user")

element = driver.find_element(By.ID, "password")
element.clear()
element.send_keys("secret_sauce")

element = driver.find_element(By.ID, "login-button")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "react-burger-menu-btn")
element.click()
time.sleep(2)

element = driver.find_element(By.CLASS_NAME, "inventory_sidebar_link")
element.click()
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "about_sidebar_link")
element.click()
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "reset_sidebar_link")
element.click()
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "logout_sidebar_link")
element.click()
