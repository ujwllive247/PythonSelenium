# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
#
# driver.maximize_window()
#
# driver.get("http://omayo.blogspot.com/")
#
# element = driver.find_element(By.ID,"testdoubleclick")
#
# actions = ActionChains(driver)
#
# actions.double_click(element).perform()
#
# time.sleep(5)
#
# # driver.quit()