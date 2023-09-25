import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

#searching

driver.find_element(By.XPATH,value="//input[@type='search']").send_keys("to")
time.sleep(10)
driver.implicitly_wait(10)

veggies =  driver.find_elements(By.XPATH,value="//div[@class='products']/div")

for i in veggies:
    print(i.text)

for j in veggies:
    j.find_element(By.XPATH,value="div[3]/button").click()

driver.find_element(By.XPATH,value="//img[@alt='Cart']").click()

driver.find_element(By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH,value="//input[@class='promoCode']").send_keys("rahulshettyacademy")


driver.find_element(By.XPATH,value="//button[@class='promoBtn']").click()
time.sleep(10)

element=WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[@class='promoInfo']")))

#TotalmAmount

Tot=driver.find_element(By.XPATH,value="//span[@class='totAmt']").text

Disc_tot=driver.find_element(By.XPATH,value="//span[@class='discountAmt']").text

assert int(Tot) > float(Disc_tot)


driver.find_element(By.XPATH,value="//button[text()='Place Order']").click()

con=Select(driver.find_element(By.XPATH,value="//select[@style='width: 200px;']"))
con.select_by_visible_text("Afghanistan")
time.sleep(3)
con.select_by_visible_text("Angola")
time.sleep(4)
con.select_by_visible_text("India")
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@class='chkAgree']").click()

driver.find_element(By.XPATH,value="//button[text()='Proceed']").click()

time.sleep(3)