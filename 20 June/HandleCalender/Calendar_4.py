import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")



driver.find_element(By.ID,"datepicker").click()

wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located(("ui-datepicker-div")))

current_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text

current_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text

while not (current_month.__eq__("August") and current_year.__eq__("2022")):
    driver.find_element(By.XPATH,"//span[text()='Prev']").click()
    current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text


driver.find_element(By.XPATH,"//td[@data-handler='selectDay']/a[text()='17']").click()

time.sleep(3)

driver.quit()

