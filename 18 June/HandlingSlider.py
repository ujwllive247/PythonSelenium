import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://omayo.blogspot.com/p/page3.html")

min_Level = driver.find_element(By.XPATH,"//a[@aria-labelledby ='price-min-label']")

time.sleep(3)

actions = ActionChains(driver)

actions.drag_and_drop_by_offset(min_Level,50,0)

# For left move , we should use -x like - 50 etc.

time.sleep(3)

driver.quit()
