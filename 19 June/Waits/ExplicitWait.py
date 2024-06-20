# import time
#
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.maximize_window()
#
# driver.get("https://omayo.blogspot.com/")
#
# driver.find_element(By.CLASS_NAME, "dropbtn").click()
#
# wait = WebDriverWait(driver, 30)
# flip_option = wait.until(expected_conditions, visibility_of_element_located((By.LINK_TEXT, "Flipkart")))
#
# flip_option.click()
#
# time.sleep(3)
#
# driver.quit()



 
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

driver.find_element(By.CLASS_NAME, "dropbtn").click()

wait = WebDriverWait(driver, 30)
flip_option = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Flipkart")))

flip_option.click()

time.sleep(3)

driver.quit()

