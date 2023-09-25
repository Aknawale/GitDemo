import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,value="//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(6)
fruits = driver.find_elements(By.XPATH,value="//div/div[@class='products']/div")

# for fruit in fruits:
#     print(fruit.text)

for i in fruits:
    i.find_element(By.XPATH,value="div/button").click()

for j in fruits:
    jj=j.find_element(By.XPATH,value="h4").text
    print(jj)

time.sleep(5)

driver.find_element(By.XPATH,value="//img[@alt='Cart']").click()
driver.find_element(By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(3)


#CODE

driver.find_element(By.XPATH,value="//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,value="//button[text()='Apply']").click()
time.sleep(15)
success_message = driver.find_element(By.XPATH,value="//span[@class='promoInfo']").text
print(success_message)

#TOTAL AMOUNT

Tot=0
price = driver.find_elements(By.XPATH,value="//tbody/tr/td[5]/p")
for i in price:
    Tot = Tot+int(i.text)

print("The Total Amount as per Actual Total is:-",Tot)

Total_Amount =  driver.find_element(By.XPATH,value="//span[@class='totAmt']")
assert Tot == int(Total_Amount.text)

Discount = driver.find_element(By.XPATH,value="//span[@class='discountAmt']")

assert int(Discount.text) < Tot
driver.find_element(By.XPATH,value="//button[text()='Place Order']").click()




