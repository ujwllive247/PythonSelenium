import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox()
# driver.maximize_window()

driver.get("http://omayo.blogspot.com/")

time.sleep(3)

element = driver.find_element(By.XPATH,"//table[@id='table1']//tbody/tr[2]/td[3]")

print(element.text)

driver.quit()

