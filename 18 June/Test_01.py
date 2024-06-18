import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("https://www.hikvision.com/en/support/how-to/how-to-video/")

action = ActionChains(driver)

Support = driver.find_element(By.LINK_TEXT,"Solutions")

action.move_to_element(Support).perform()

time.sleep(3)

driver.quit()