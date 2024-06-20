
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

for i in range(1,6):
    xpath_text = "(//div[@id='LinkList1']//a)["+str(i)+"]"

    time.sleep(2)

    driver.find_element(By.XPATH,xpath_text).click()
    time.sleep(2)
    driver.back()


driver.quit()