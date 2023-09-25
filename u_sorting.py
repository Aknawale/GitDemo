import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,value="//span[@class='sort-icon sort-descending']").click()
time.sleep(3)

foods = driver.find_elements(By.XPATH,value="//tbody/tr/td[1]")
foodlist=[]
for i in foods:
    foodlist.append(i.text)
print(foodlist)
type(foodlist)

new_sorted = foodlist
new_sorted.sort()
time.sleep(3)
print("SORTED List Is:-", new_sorted)

assert new_sorted == foodlist

