import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.set_page_load_timeout(2)

driver.get("https://omayo.blogspot.com/")

Links = driver.find_elements(By.XPATH,"//a")

print(len(Links))

for i in Links:
    print(i.get_attribute("href"))           # For loop is used to print the the all elements....

driver.quit()