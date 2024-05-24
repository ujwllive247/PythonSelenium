import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


# Open the url...

driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.XPATH,"//input[@value='Login']").click()

# CSS Selector.........

driver.find_element(By.CSS_SELECTOR,"input[value='Login'] ").click()

time.sleep(3)
driver.quit()





#//input[@value="Login"]      Xpath...........
#input[value="Login"]         CSS Selector........