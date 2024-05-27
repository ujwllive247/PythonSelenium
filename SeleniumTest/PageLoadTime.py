import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.set_page_load_timeout(2)

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

driver.quit()