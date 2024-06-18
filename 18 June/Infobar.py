import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options



Firefox_options =Options()

Firefox_options.add_experimental_option("exludeSwitches",["enable-automation"])

Firefox_options.add_experimental_option("useAutomationExtention",False)

Firefox_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Firefox(Options=Firefox_options)


driver.get("https://tutorialsninja.com/demo/")

# Chrome is being controlled by test automation software.

print(driver.title)

time.sleep(3)

driver.quit()