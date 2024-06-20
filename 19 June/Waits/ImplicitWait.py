
import time
from webdriver_manager.chrome import ChromeDriverManager


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)    #Global Wait
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME,"dropbtn").click()

# time.sleep(3) # Hard wait

driver.find_element(By.LINK_TEXT,"Flipkart").click()



driver.quit()


# Implicit wait applied on all the script which is written below..In this case , there is
# an issue in wrong locator.....