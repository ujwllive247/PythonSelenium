# URL - https://www.homedepot.com/


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--guest")

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get(" https://www.homedepot.com/")

time.sleep(5)

driver.quit()


