from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.demo.guru99.com/popup.php")
time.sleep(5)
try:
    element = WebDriverWait(driver, 25, 1).until(EC.visibility_of_element_located((By.NAME, "akshay")))
    element.click()


except Exception:
    print("error for element not found")

driver.quit()