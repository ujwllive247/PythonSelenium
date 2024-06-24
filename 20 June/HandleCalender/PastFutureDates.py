import datetime
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
wait.until(EC.visibility_of_element_located((By.ID,"ui-datepicker-div")))

expected_date = "2024-09-27"



formatted_date = datetime.strptime("%Y-%m-%d")



#Programme not completed yet....