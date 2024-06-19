import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.find_element(By.ID,"input-firstname").send_keys("Ujjwal")

actions = ActionChains(driver)

actions.send_keys(Keys.TAB).pause(3).send_keys("Thakur").send_keys(Keys.TAB).pause(3).send_keys("Ujj@email.com").send_keys(Keys.TAB).pause(3).perform()



driver.quit()