import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,value="//input[@id='autosuggest']").send_keys("po")
time.sleep(3)

countries = driver.find_elements(By.XPATH,value="//ul/li[@class='ui-menu-item']/a")

print(len(countries))

time.sleep(3)
for country in countries:
    if(country.text=="Poland"):
        country.click()
        time.sleep(10)
        break


message = driver.find_element(By.XPATH,value="//input[@id='autosuggest']").get_attribute("value")

assert message == "Poland"
time.sleep(3)







