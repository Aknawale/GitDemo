import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver=webdriver.Chrome(service=service_obj,options=chrome_options)





driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
driver.find_element(By.TAG_NAME,"p").clear()
time.sleep(3)
driver.find_element(By.TAG_NAME,"p").send_keys("I am rewriting in the text box")
time.sleep(10)

driver.switch_to.default_content()
time.sleep(3)
print(driver.find_element(By.XPATH,value="//div/h3").text)
time.sleep(3)




