from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver = webdriver.Chrome('/Users/fxrxbx/Downloads/chromedriver')

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

element = driver.find_element(By.ID, "item_4_img_link")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "item_0_img_link")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "item_5_img_link")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "checkout")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "continue-shopping")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
element.click()
time.sleep(3)


element = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "checkout")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "first-name")
element.clear()
element.send_keys("Eddy")

element = driver.find_element(By.ID, "last-name")
element.clear()
element.send_keys("Jones")

element = driver.find_element(By.ID, "postal-code")
element.clear()
element.send_keys("2345")

element = driver.find_element(By.ID, "continue")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "finish")
element.click()
time.sleep(3)
element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "react-burger-menu-btn")
element.click()
time.sleep(2)

element = driver.find_element(By.ID, "about_sidebar_link")
element.click()
time.sleep(3)

driver.back()

element = driver.find_element(By.ID, "item_4_img_link")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "react-burger-menu-btn")
element.click()
time.sleep(2)

element = driver.find_element(By.ID, "reset_sidebar_link")
element.click()
time.sleep(3)


element = driver.find_element(By.ID, "inventory_sidebar_link")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "logout_sidebar_link")
element.click()