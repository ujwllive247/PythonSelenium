import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

dropdown_field = driver.find_element(By.ID,"drop1")

Select = Select(dropdown_field)

Select.select_by_index(3)   # handle dropdown using _index>>...

Select.select_by_value()    # Also, handle by _ Value....






