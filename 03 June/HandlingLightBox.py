import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&product_id=43")

time.sleep(3)
driver.find_element(By.XPATH,"(//img[@title='MacBook'])[1]").click()

time.sleep(3)

driver.find_element(By.XPATH,"//button[@title='Close (Esc)']").click()

time.sleep(3)

driver.quit()