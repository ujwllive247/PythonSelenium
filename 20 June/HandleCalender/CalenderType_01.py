

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

time.sleep(3)

driver.find_element(By.ID,"datepicker").click()

wait = WebDriverWait(driver,5)

wait.until(EC.visibility_of_element_located((By.ID,"ui-datepicker-div")))

Current_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text

Current_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")

while not Current_month.__eq__("November") and Current_year.__eq__("2024"):
    driver.find_element(By.XPATH,"//span[text()='Next']").click()
    Current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    Current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")

driver.find_element(By.XPATH," //td[@data-handler='selectDay']/a[text()='25']").click()

time.sleep(3)

driver.quit()
