from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, value="autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.XPATH,value=("//li[@class='ui-menu-item']/a"))

print(len(countries))
print(countries)
#print(countries)
time.sleep(3)

for i in countries:
    if(i.text =="India"):
        i.click()
        print("option is selected successfully")
        break
    else:
        pass

assert driver.find_element(By.ID, value="autosuggest").get_attribute("value") == "India"







