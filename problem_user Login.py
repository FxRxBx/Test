from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('/Users/fxrxbx/Downloads/chromedriver')

driver.get("https://qa-challenge.codesubmit.io/")

element = driver.find_element(By.ID, "user-name")
element.clear()
element.send_keys("problem_user")

element = driver.find_element(By.ID, "password")
element.clear()
element.send_keys("secret_sauce")

element = driver.find_element(By.ID, "login-button")
element.click()

#PLEASE NOTE : the code below will not be functional due to the various issues listed in the README file.

element = driver.find_element(By.ID, "item_4_img_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "item_0_img_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "item_5_img_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
element.click()
time.sleep(1)

element = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "continue-shopping")
element.click()
time.sleep(1)

select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_visible_text("Price (low to high)")
time.sleep(1)
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value('az')
time.sleep(1)
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_visible_text("Price (high to low)")
time.sleep(1)
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value('za')
time.sleep(1)

element = driver.find_element(By.ID, "item_1_title_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "item_3_title_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "item_2_title_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "item_4_img_link")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "remove-sauce-labs-backpack")
element.click()
time.sleep(1)

element = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "checkout")
element.click()
time.sleep(3)

element = driver.find_element(By.ID, "first-name")
element.clear()
element.send_keys("TIM")

element = driver.find_element(By.ID, "last-name")
element.clear()
element.send_keys("Jons")

element = driver.find_element(By.ID, "postal-code")
element.clear()
element.send_keys("2345")

element = driver.find_element(By.ID, "continue")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "finish")
element.click()
time.sleep(1)
element = driver.find_element(By.ID, "back-to-products")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "react-burger-menu-btn")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "about_sidebar_link")
element.click()
time.sleep(1)

driver.back()
time.sleep(1)

element = driver.find_element(By.ID, "item_4_img_link")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "react-burger-menu-btn")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "reset_sidebar_link")
element.click()
time.sleep(1)

element = driver.find_element(By.ID, "logout_sidebar_link")
element.click()

