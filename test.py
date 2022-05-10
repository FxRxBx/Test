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

if(driver.findElement(By.id("reports").size()!=0){

   WebElement menuHoverLink = driver.findElement(By.id("reports"));
   actions.moveToElement(menuHoverLink).perform();

   }
   else{
   system.out.println("element not present -- so it entered the else loop");

}