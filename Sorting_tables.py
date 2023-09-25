from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
sortedlist=[]
time.sleep(3)

driver.find_element(By.XPATH,value="//span[text()='Veg/fruit name']").click()

list = driver.find_elements(By.XPATH,value="//tr/td[1]")
print(list)
for i in list:
    sortedlist.append(i.text)

orignalsorted_list = sortedlist

print("OrginalList is:-", orignalsorted_list)
print("Sorted List is:-", sortedlist)

sortedlist.sort()

time.sleep(5)
assert orignalsorted_list == sortedlist

