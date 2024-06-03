import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://selenium143.blogspot.com/")

driver.find_element(By.LINK_TEXT,"What is Selenium?").click()



# We can set the load time for opening the web url....