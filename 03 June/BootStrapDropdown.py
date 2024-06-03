


# xpath -    //button[@id='dropdownMenuButton']/following-sibling::div/a[1]



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://getbootstrap.com/docs/4.0/components/dropdowns/")

time.sleep(3)

driver.find_element(By.ID,"dropdownMenuButton").click()

time.sleep(3)

driver.find_element(By.XPATH," //button[@id='dropdownMenuButton']/following-sibling::div/a[1]").click()

driver.quit()

