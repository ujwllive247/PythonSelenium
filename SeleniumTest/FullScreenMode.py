import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

time.sleep(2)

driver.fullscreen_window()

time.sleep(2)


driver.quit()