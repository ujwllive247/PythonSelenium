#https://tutorialsninja.com/demo/


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()

# Open the url...

driver.get("https://tutorialsninja.com/demo/")
driver.find_element(By.XPATH,"//span[text()='My Account']").click()
driver.find_element(By.LINK_TEXT,"Login").click()

time.sleep(3)
driver.find_element(By.ID, "input-email").send_keys("ujwllive247@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("Kangaroo@123")
driver.find_element(By.XPATH,"//input[@value='Login']").click()


if driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed():
    print("Login Verified....")
else:
    print("User not able to Login")


driver.quit()














time.sleep(2)
driver.quit()