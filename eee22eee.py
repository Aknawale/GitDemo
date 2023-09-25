import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.edge.service import Service as EdgeService
service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH,value="//input[@type='search']").send_keys("er")


veggies = driver.find_elements(By.XPATH,value="//div[@class='product']")

for i in veggies:
    i.find_element(By.XPATH,value="div[3]/button").click()
    time.sleep(2)

driver.find_element(By.XPATH,value="//a[@class='cart-icon']").click()
driver.find_element(By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

#PROMOCODE
driver.find_element(By.XPATH,value="//input[@class='promoCode']").send_keys("rahulshettyacademy")
time.sleep(10)
driver.find_element(By.XPATH,value="//button[@class='promoBtn']").click()

time.sleep(10)
elements = WebDriverWait(driver,10)
elements.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))

print(driver.find_element(By.CLASS_NAME,value="promoInfo").text)
Total_amt = int(driver.find_element(By.XPATH,value="//span[@class='totAmt']").text)

disc_amt = float(driver.find_element(By.XPATH,value="//span[@class='discountAmt']").text)

assert Total_amt > disc_amt


Amount = driver.find_elements(By.XPATH,value="//td[5]/p")
s=0
for i in Amount:
    s=int(i.text)+s
print("The Total sum as per calculation is:p-",s)

assert s==Total_amt, "There is error in the count"

l1=['Cauliflower - 1 Kg','Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg','Water Melon - 1 Kg']

new_li = driver.find_elements(By.XPATH,value="//td[2]/p")
ff=[]
for i in new_li:
    ff.append(i.text)
print(ff)


assert l1 == ff, "error in the fetched list"
driver.find_element(By.XPATH,value="//button[text()='Place Order']").click()
time.sleep(3)