import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://jqueryui.com/resizable/")

frame_one = driver.find_element(By.CLASS_NAME,"demo-frame")

driver.switch_to.frame(frame_one)

action = ActionChains(driver)

dragdrop = driver.find_element(By.CSS_SELECTOR,"div.ui-icon-gripsmall-diagonal-se")

action.drag_and_drop_by_offset(dragdrop,50,50).perform()

time.sleep(4)

driver.quit()