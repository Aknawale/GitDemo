from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/client/auth/login")

time.sleep(4)

driver.find_element(By.LINK_TEXT,value="Forgot password?").click()

time.sleep(4)

driver.find_element(By.XPATH,value="//form/div[1]/input").send_keys("demo@gmail.com")

time.sleep(4)

driver.find_element(By.XPATH, value="//form/div[2]/input").send_keys("")