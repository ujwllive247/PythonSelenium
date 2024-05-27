

# Retreving html attribute value......

import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
# driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")
# c =driver.find_element(By.ID ,"ta1").get_attribute("cols")            # Retrieving the cols      value.....

d = driver.find_element(By.XPATH, "(//input[@title='search'])[2]").get_attribute("value")
print(d)


time.sleep(2)
driver.quit()