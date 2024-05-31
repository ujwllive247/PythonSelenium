import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

time.sleep(3)

Prompt_Alert = driver.switch_to.alert

print(Prompt_Alert.text)

Prompt_Alert.send_keys("Hello, this is ujjwal")

time.sleep(6)

Prompt_Alert.accept()




time.sleep(3)

driver.quit()