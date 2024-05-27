import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# Open the url...

driver.get("https://omayo.blogspot.com/")

Title_of_page = driver.title
print(Title_of_page)


Tile_of_page_two =driver.find_element(By.LINK_TEXT ,"compendiumdev").click()

driver.title
print(Tile_of_page_two)       # This will print the title of second page......

time.sleep(2)
driver.quit()