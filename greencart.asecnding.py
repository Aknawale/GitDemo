from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService


service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
appended_list=[]
driver.find_element(By.XPATH,value="//tr/th[1]/span[1]").click()
new_sort=[]
browser_list = driver.find_elements(By.XPATH,value="//tr/td[1]")
for i in browser_list:
    appended_list.append(i.text)

new_sortt=appended_list.copy()

appended_list.sort()

assert appended_list == new_sortt,"the ascending order is not meet"