import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

Multi_Selection_Box =driver.find_element(By.ID,"multiselect1")

select = Select(Multi_Selection_Box)

m_option = select.options

print(type(m_option))       #<class 'list'>


for option in m_option:
    print(option.text)




driver.quit()