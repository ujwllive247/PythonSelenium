import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

blogs = driver.find_element(By.ID,"blogsmenu")

actions = ActionChains(driver)

actions.move_to_element(blogs).perform()

time.sleep(3)

selenium_byarun =driver.find_element(By.XPATH,"//a/span[text()='SeleniumOneByArun']")

time.sleep(3)

actions.move_to_element(selenium_byarun).perform()

driver.quit()

