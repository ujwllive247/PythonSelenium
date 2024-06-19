import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.makemytrip.com/")

time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/span").click()

time.sleep(3)

driver.find_element(By.ID,"fromCity").click()

driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("gorakhpur")

actions = ActionChains(driver)

actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

time.sleep(3)


driver.quit()