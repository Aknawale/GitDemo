from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
nnewsorted=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,value="//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
time.sleep(2)

Browser_sorted = driver.find_elements(By.XPATH,value="//tbody/tr/td[1]")
time.sleep(2)
for i in Browser_sorted:
    nnewsorted.append(i.text)

Browser_sorted_copy = nnewsorted.copy()
time.sleep(3)
nnewsorted.sort()
time.sleep(2)
assert nnewsorted == Browser_sorted_copy

time.sleep(4)

driver.close()





