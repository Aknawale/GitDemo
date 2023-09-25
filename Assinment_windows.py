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

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,value="Free Access to InterviewQues/ResumeAssistance/Material").click()

time.sleep(3)

windows = driver.window_handles

driver.switch_to.window(windows[1])
time.sleep(3)
emaill =  driver.find_element(By.XPATH,value="//div/p[2]").text
time.sleep(3)
up1=emaill.split("at")
time.sleep(3)
print(up1)

email = up1[1]
print(email)

maill = email.split("with")
print(maill)

final_maill = maill[0]
finalmail=final_maill.strip()
print(finalmail)
time.sleep(4)

driver.switch_to.window(windows[0])

driver.find_element(By.ID,value="username").send_keys(finalmail)
time.sleep(3)
driver.find_element(By.ID,value="password").send_keys("PASSWORD")
time.sleep(3)
driver.find_element(By.ID,value="terms").click()
time.sleep(3)






