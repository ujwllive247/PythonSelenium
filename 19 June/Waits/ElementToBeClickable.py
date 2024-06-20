
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

driver.find_element(By.XPATH,"//button[text()='Check this']").click()

wait = WebDriverWait(driver,12)

Check_Box_field = wait.until(EC.element_to_be_clickable((By.ID,"dte")))

Check_Box_field.click()

time.sleep(3)

driver.quit()