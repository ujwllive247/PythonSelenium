
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

time.sleep(3)

driver.find_element(By.ID,"input-email").send_keys("Ujwllive247@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("Kangaroo@123")
time.sleep(3)
driver.find_element(By.ID,"input-password").send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()