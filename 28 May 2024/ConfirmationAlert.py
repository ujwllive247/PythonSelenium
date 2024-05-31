import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()

time.sleep(3)

Confirmation_Alert = driver.switch_to.alert

print(Confirmation_Alert.text)


# Confirmation_Alert.accept()

Confirmation_Alert.dismiss()       # For dismiss method , Cancel button clicked.....

time.sleep(3)

driver.quit()