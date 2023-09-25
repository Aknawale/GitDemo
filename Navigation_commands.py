from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.moneycontrol.com/")

time.sleep(11)

#driver.find_element(By.link_text, value="moneycontrol.com").click()
#time.sleep(3)

driver.find_element(By.LINK_TEXT, value="Commodities").click()

driver.back()

time.sleep(3)


driver.forward()

time.sleep(3)

driver.refresh()

time.sleep(3)

driver.quit()