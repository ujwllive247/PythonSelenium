
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://omayo.blogspot.com/")

driver.find_element(By.XPATH,"//div[@id='LinkList']//a")