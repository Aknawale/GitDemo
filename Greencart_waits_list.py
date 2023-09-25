from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,value="//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

fruitss = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
fruits_lst = driver.find_elements(By.XPATH,value="//div/div/h4")
l=[]
flag=0
for j in fruits_lst:
    print("the added fruits are as below:-", j.text)
    l.append(j.text)
print("Total Appended list:-", l)
print("Original fruits list :-",fruitss)

assert fruitss == l,"List is not equal"

# if(flag==1):
#     print('List is not equal')
# else:
#     print("List of Expected and Actual is equal")






products = driver.find_elements(By.XPATH,value="//div[@class='products']/div")

print("The Total products added in List are:-", len(products))

for i in products:

    i.find_element(By.XPATH,value="div/button").click()


driver.find_element(By.XPATH,value="//img[@alt='Cart']").click()

driver.find_element(By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CLASS_NAME,value="promoCode").send_keys("rahulshettyacademy")


driver.find_element(By.XPATH,value="//button[@class='promoBtn']").click()

wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, '.promoInfo'))
time.sleep(10)

message = driver.find_element(By.CLASS_NAME,value="promoInfo").text

assert message == "Code applied ..!"

prices = driver.find_elements(By.XPATH, value="//tr/td[5]/p")
summ=0
for price in prices:
    summ = summ+int(price.text)
print("the Sum as per Table is:-", summ)

aaa = int(driver.find_element(By.XPATH,value="//span[@class='totAmt']").text)

assert aaa == summ

After_disc = float(driver.find_element(By.XPATH,value = "//span[@class = 'discountAmt']").text)
print("After Discount price is:-",After_disc)

assert After_disc < aaa , "After Discount value is greater than actual price"


driver.find_element(By.XPATH,value="//button[text()='Place Order']").click()






