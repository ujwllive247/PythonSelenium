import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

time.sleep(3)

JqueryButton =driver.find_element(By.XPATH,"//span[text()='right click me']")

actions = ActionChains(driver)

actions.context_click(JqueryButton).perform()

time.sleep(3)

Quit_option = driver.find_element(By.XPATH,"//li/span[text()='Quit']")

actions.context_click(Quit_option).perform()

time.sleep(3)

driver.quit()
