import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

Text_area_field_one =driver.find_element(By.ID,"ta1")
Text_area_field_one.send_keys("Twinkle Twinkle little star")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()

time.sleep(3)

driver.back()

time.sleep(3)

Text_area_field_one = driver.find_element(By.ID,"ta1")  # We need to assign the value again.before performing the action.

Text_area_field_one.clear()   # This is not able to find the web element when we comeback to that page.


time.sleep(3)

driver.quit()

