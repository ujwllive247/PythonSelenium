import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")
driver.find_element(By.LINK_TEXT ,"compendiumdev").click()

time.sleep(3)
driver.quit()