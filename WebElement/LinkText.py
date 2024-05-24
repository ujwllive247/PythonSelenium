import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")

# CSS Selector.........

Link = driver.find_element(By.ID,'selenium143').click()


time.sleep(3)
driver.quit()