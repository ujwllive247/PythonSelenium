import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")

Current_Url =driver.current_url
print(Current_Url)


time.sleep(2)


#Difference between quit and close window........
driver.quit()   # Quit command closed the all window.....

driver.close()       # close command , only close the current window.....