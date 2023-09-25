import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)
#
# service_obj= Service("F:\Selenium_Data\Firefox_driver\geckodriver-v0.33.0-win-aarch64\geckodriver.exe")
#
# driver=webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/")

print(driver.title)

time.sleep(3)

print(driver.current_url)

time.sleep(3)

assert driver.title == "Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy"

assert driver.current_url == "https://rahulshettyacademy.com/"

time.sleep(3)