import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

driver.maximize_window()

mobiles= driver.find_elements(By.XPATH,value="//div/app-card-list/app-card/div[1]")

for i in mobiles:
    if (i.find_element(By.XPATH,value="div/h4/a").text== "Blackberry"):
        i.find_element(By.XPATH,value="div[2]/button").click()
        time.sleep(5)
    else:
        pass

driver.find_element(By.XPATH,value="//a[@class='nav-link btn btn-primary']").click()

time.sleep(4)

driver.find_element(By.XPATH,value="//button[@class='btn btn-success']").click()
driver.find_element(By.ID,value="country").send_keys("ind")


wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'India')))
country = Select(driver.find_element(By.CLASS_NAME, value="validate filter-input"))

country.select_by_visible_text("India")
time.sleep(5)

