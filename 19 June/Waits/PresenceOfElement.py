

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME,"dropbtn").click()

wait = WebDriverWait(driver,30)
hidden_button =wait.until(EC.presence_of_element_located((By.ID,"hbutton")))
hidden_button_label = hidden_button.get_attribute("value")
print(hidden_button_label)

time.sleep(3)

driver.quit()