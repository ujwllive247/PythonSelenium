

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.set_page_load_timeout(2)

driver.get("https://omayo.blogspot.com/")

options =driver.find_elements(By.XPATH,"//select[@id='multiselect1']//option")

for i in options:
    print(i.text)           # For loop is used to print the the all elements....

driver.quit()