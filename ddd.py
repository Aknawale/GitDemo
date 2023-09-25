import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.select import Select

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.ID,value="autosuggest").send_keys("ind")

time.sleep(3)

countries = driver.find_elements(By.XPATH,value="//li[@class='ui-menu-item']/a")
print(len(countries))
for i in countries:
    if(i.text=="India"):
        i.click()
        time.sleep(4)
    else:
        pass
