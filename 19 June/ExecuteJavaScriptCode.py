import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.execute_script("alert('Ujjwal')")

time.sleep(3)
driver.quit()