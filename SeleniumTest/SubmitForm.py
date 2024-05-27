import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

driver.find_element(By.ID, "input-email").submit()

time.sleep(2)

driver.fullscreen_window()

time.sleep(2)


driver.quit()