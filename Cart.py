import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.implicitly_wait(15)


driver.find_element(By.XPATH,value="//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

fruit_list = (driver.find_elements(By.XPATH,value="//div/h4[@class = 'product-name']"))
original_fruit_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
assert fruit_list == original_fruit_list

fruits = driver.find_elements(By.XPATH,value="//div/div[@class='products']/div")
for i in fruits:
    print(i.text)

for fruit in fruits:
    fruit.find_element(By.XPATH,value="div/button").click()
    time.sleep(2)

time.sleep(2)

driver.find_element(By.XPATH,value="//img[@alt='Cart']").click()

driver.find_element(By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(5)

driver.find_element(By.XPATH,value="//input[@class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH,value="//button[@class='promoBtn']").click()

time.sleep(10)


wait =WebDriverWait(driver,15)


wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


messagee = driver.find_element(By.XPATH,value="//span[@class='promoInfo']").text

assert messagee == "Code applied ..!"

Totalll = driver.find_elements(By.XPATH,value="//tbody/tr/td[5]/p[@class='amount']")
summ=0
for i in Totalll:
    print(i.text)
    summ=summ+int(i.text)

print("the sum is:-",summ)

time.sleep(5)

TotalAmount = int(driver.find_element(By.XPATH,value="//span[@class='totAmt']").text)
print("The Total Bill amount is:-",TotalAmount)
time.sleep(3)

discounted = float(driver.find_element(By.XPATH,value="//span[@class='discountAmt']").text)
print("The Discounted Bill amount is:-",discounted)
time.sleep(3)

assert discounted < TotalAmount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

time.sleep(3)