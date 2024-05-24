#radio1

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")

# CSS Selector.........
driver.find_element(By.ID,'ta1').send_keys("This is the Web Automation task")


time.sleep(3)
driver.quit()