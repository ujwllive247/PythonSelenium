import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

male_Radio_button = driver.find_element(By.ID,"radio1")

if male_Radio_button.is_selected():
    pass
else:
    male_Radio_button.click()


driver.quit()

print("Testcase passed")

