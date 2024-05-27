import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")

Current_Url =driver.current_url
print(Current_Url)

# driver.find_element(By.LINK_TEXT,"compendiumdev").click()
#
# SecondPage_url =driver.current_url
#
# print(SecondPage_url)






time.sleep(2)
driver.quit()