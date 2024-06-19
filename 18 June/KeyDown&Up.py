# Ctrl + click on the link , open the link other tab...



import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://omayo.blogspot.com/")

links =driver.find_element(By.XPATH,"//div[@id='LinkList1']//a")   #  '//*[@href]'    #

for link in links:
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


time.sleep(5)

driver.quit()