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
driver.find_element(By.CLASS_NAME ,"dropbtn").click()

time.sleep(3)
driver.quit()