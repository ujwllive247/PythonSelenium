

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")
driver.save_screenshot("Browser.png")




time.sleep(3)
driver.quit()