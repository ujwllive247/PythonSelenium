import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()

time.sleep(3)

info_alert = driver.switch_to.alert
print(info_alert.text)

info_alert.accept()

# info_alert.dismiss()   # We can also use the dismiss command ....


time.sleep(3)


driver.quit()
