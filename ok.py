import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH,value="//input[@value='radio1']").click()
time.sleep(4)

driver.find_element(By.CSS_SELECTOR,value="input[value='radio2']").click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,value="input[value='radio3']").click()

time.sleep(3)