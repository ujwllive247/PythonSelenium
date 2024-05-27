
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")

if driver.find_element(By.ID,"but2").is_enabled():
    print("Button 2 is in enable state.....")

else:                                          # Else is used for verifying the disable button.....
    print("Button 2 is in disable state")





time.sleep(2)
driver.quit()