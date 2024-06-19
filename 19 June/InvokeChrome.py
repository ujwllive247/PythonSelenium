

import time
from webdriver_manager.chrome import ChromeDriverManager


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.execute_script("alert('Ujjwal')")

time.sleep(3)   #Hard Wait
driver.quit()