# Checking the particular element is present or not on the web page...



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")

# if driver.find_element(By.ID, "ta1").is_displayed():

check = driver.find_element(By.ID, "ta1").is_displayed()
if check:
    print("Text area field is present on the page.")
else:
    print("Not displayed")


driver.quit()    
