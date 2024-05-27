
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")

# driver.get("https://facebook.com/")

if driver.find_element(By.ID,"checkbox1").is_selected():
    print("Orange radio button is selected.....")

else:                                          # Else is used for verifying the disable button.....
    print("Not selected.....")


# driver.back()
# driver.forward()
# driver.refresh()






time.sleep(2)
driver.quit()