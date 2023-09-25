import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

options = driver.find_elements(By.XPATH,value="//div/fieldset/label/input[@type='checkbox']")
print(len(options))
for option in options:
    if option.get_attribute("value")=="option1":
        option.click()
        time.sleep(4)
        assert option.is_selected()
        break


radio = driver.find_elements(By.XPATH,value="//div/fieldset/label/input[@name='radioButton']")
print(len(radio))

for ra in radio:
    if ra.get_attribute("value") == "radio1":
        ra.click()
        time.sleep(3)
        assert ra.is_selected()

assert driver.find_element(By.ID,value="displayed-text").is_displayed()

driver.find_element(By.ID,value="hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID,value="displayed-text").is_displayed()
time.sleep(5)


driver.find_element(By.ID,value="alertbtn").click()

alerts = driver.switch_to.alert
print(alerts.text)
time.sleep(3)
alerts.accept()

driver.find_element(By.ID,value="name").send_keys("AKSHAY")
time.sleep(3)
driver.find_element(By.ID,value="confirmbtn").click()
alerts = driver.switch_to.alert
texxt = alerts.text
print(alerts.text)
time.sleep(2)
alerts.accept()

assert "AKSHAY" in texxt
