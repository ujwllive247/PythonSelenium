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

table_headings = driver.find_elements(By.XPATH,"//table[@id='table1']//th")

for heading in table_headings:
    print(heading.text)


driver.quit()
