# Printing the entire source code...............



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

Html_source_code = driver.page_source        # Printing the entire html page source code..........
print(Html_source_code)


driver.quit()
