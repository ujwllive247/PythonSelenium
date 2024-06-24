# Author - Ujjwal Thakur
# Objective - In this script, we are trying to print the first row data from the table.
# Url - http://omayo.blogspot.com



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox()
# driver.maximize_window()

driver.get("http://omayo.blogspot.com/")

table_data = driver.find_elements(By.XPATH,"//table[@id='table1']//tbody/tr[2]/td")        # We can print the data from any row ..just changing the tr[] value..

for data in table_data:
    print(data.text)


driver.quit()