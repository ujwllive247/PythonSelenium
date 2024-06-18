
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()



driver.get("https://tutorialsninja.com/demo/")

search = driver.find_element(By.NAME,"search")

time.sleep(3)

actions = ActionChains(driver)

actions.context_click(search).perform()

time.sleep(3)

driver.quit()