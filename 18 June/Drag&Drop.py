import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")

oslo = driver.find_element(By.ID,"box1")

Norway = driver.find_element(By.ID,"box101")

action = ActionChains(driver)

action.drag_and_drop(oslo,Norway).perform()

time.sleep(3)

driver.quit()