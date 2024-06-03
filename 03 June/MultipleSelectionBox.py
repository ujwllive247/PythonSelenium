import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

Multi_Selection_Box =driver.find_element(By.ID,"multiselect1")

select = Select(Multi_Selection_Box)

select.select_by_index(2)

select.select_by_value("volvox")

select.select_by_visible_text("Swift")


# We can also do deselect command on the multi_selection_box......

select.deselect_all()


time.sleep(4)




driver.quit()
