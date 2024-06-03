

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,"justAnInputBox").click()

driver.find_element(By.XPATH,"(//span[contains(text(),'choice 3')])[1]").click()

time.sleep(2)



driver.find_element(By.XPATH,"(//span[contains(text(),'choice 5')])[1]").click()

time.sleep(3)


driver.find_element(By.XPATH,"//div[@id='jquery-script-menu']/following-sibling::div/h1").click()

time.sleep(3)

driver.quit()

