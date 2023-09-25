import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.select import Select

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.XPATH,value="//input[@name='name']").send_keys("Akshay Nawale")
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@name='email']").send_keys("Akshay.Nawale@gmail.com")
time.sleep(3)

driver.find_element(By.ID,value="exampleInputPassword1").send_keys("PASSWORD")
time.sleep(3)

driver.find_element(By.ID,value="exampleCheck1").click()
time.sleep(4)

gen=Select(driver.find_element(By.ID,value="exampleFormControlSelect1"))

gen.select_by_visible_text("Male")
time.sleep(3)

gen.select_by_visible_text("Female")
time.sleep(3)

driver.find_element(By.ID,value="inlineRadio1").click()
time.sleep(3)


driver.find_element(By.XPATH,value="//input[@type='submit']").click()

time.sleep(3)

message = driver.find_element(By.XPATH,value="//div[@class='alert alert-success alert-dismissible']").text
print(message)
assert "Success!" in message