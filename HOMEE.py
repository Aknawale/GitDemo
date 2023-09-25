import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.maximize_window()


driver.find_element(By.CLASS_NAME,value="form-control").send_keys("AKSHAY")
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@name='email']").send_keys("AKSHAY@gmail.com")
time.sleep(4)

driver.find_element(By.CSS_SELECTOR,value="input[id='exampleInputPassword1']").send_keys("PASSWORD")
time.sleep(4)

driver.find_element(By.XPATH,value="//input[@type='checkbox']").click()
time.sleep(4)

gender=Select(driver.find_element(By.XPATH,value="//select[@class='form-control']"))
gender.select_by_visible_text("Male")
time.sleep(3)

driver.find_element(By.XPATH,value="(//input[@class='form-check-input'])[3]").click()
time.sleep(3)


driver.find_element(By.XPATH,value="//input[@value='Submit']").click()

time.sleep(3)

message=driver.find_element(By.XPATH,value="//div[@class='alert alert-success alert-dismissible']").text

assert "successful" in message

time.sleep(4)

