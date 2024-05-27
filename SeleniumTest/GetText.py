import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import service
from selenium.webdriver.edge.options import Options

# firefox_options = Options()
# firefox_options.add_argument("--headless")


driver = webdriver.Firefox()

# driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")
# Text_Heading = driver.find_element(By.ID, "pah").text        # .text command is only applicable for open and close tags....elements.
Text_Button = driver.find_element(By.Id, 'button9').text
# print(Text_Heading)
print(Text_Button)

time.sleep(2)
driver.quit()
