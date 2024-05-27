import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

Tagname_Login =driver.find_element(By.ID, "input-email").tag_name

print(Tagname_Login)    #    input



Element_size_Location = driver.find_element(By.NAME,"search").rect     # The " rect Command" print the size and location both.

# Element_location = driver.find_element(By.NAME,"search").location

# print(Element_size)       # print the size as a dictionary        {'height': 40.0, 'width': 373.5}

print(Element_size_Location)            # Print cordinates -  {'x': 460, 'y': 64}


time.sleep(2)


driver.quit()