import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

# time.sleep(3)

actions = ActionChains(driver)

blogs = driver.find_element(By.ID,"blogsmenu")

actions.move_to_element(blogs).perform()

time.sleep(3)

driver.quit()