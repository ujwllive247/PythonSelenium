import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver.Firefox()   Invoke the browser...
# webdriver.Edge()
# webdriver.Safari()


driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")
driver.find_element(By.ID ,"ta1").send_keys("My name is ujjwal, This is my first testcase")

time.sleep(2)
driver.quit()
