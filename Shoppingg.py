from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,value="Shop").click()

mobiles = driver.find_elements(By.XPATH,value="//app-card-list/app-card/div/div[1]/h4")
print("The List of mobiles is as Follows:- ")
for i in mobiles:
    print(i.text)

for i in mobiles:
    if(i.text)== "Blackberry":
        driver.find_element(By.XPATH,value="//app-card-list/app-card/div/div/button").click()

driver.find_element(By.XPATH,value="//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH,value="//button[@class='btn btn-success']").click()

driver.find_element(By.XPATH,value="//input[@id='country']").send_keys("Ind")

time.sleep(10)

wait= WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))


driver.find_element(By.LINK_TEXT,"India").click()


driver.find_element(By.XPATH,value="//label[@for='checkbox2']").click()
time.sleep(4)
driver.find_element(By.XPATH,value="//input[@value='Purchase']").click()