


import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.ID,"alert1").click()

wait = WebDriverWait(driver,5)
wait.until(EC.alert_is_present())

al = driver.switch_to.alert
alert_text = al.text

print(alert_text)

time.sleep(3)
al.accept()

driver.quit()

