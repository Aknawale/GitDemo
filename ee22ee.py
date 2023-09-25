import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT,value="Shop").click()

driver.execute_script("window.scrollBy(0,600)")
time.sleep(3)


mobiles = driver.find_elements(By.XPATH,value="//div/app-card-list/app-card")
time.sleep(3)

for mobile in mobiles:
    if (mobile.find_element(By.XPATH,value="div/div/h4").text == "Blackberry"):
        mobile.find_element(By.XPATH,value = "div/div/button").click()
        time.sleep(15)
    else:
        pass

driver.find_element(By.XPATH,value="//a[@class = 'nav-link btn btn-primary']").click()

time.sleep(4)

driver.find_element(By.XPATH,value="//button[@class = 'btn btn-success']").click()
time.sleep(4)

driver.find_element(By.XPATH,value="//input[@id='country']").send_keys("Ind")

waits = WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/ul[1]/li/a")))

waits.click()

#driver.find_element(By.XPATH,value="//label[@for='checkbox2']").click()
#time.sleep(3)

driver.find_element(By.XPATH,value="//input[@type='submit']").click()


successmessag = driver.find_element(By.XPATH,value="//div[@class='alert alert-success alert-dismissible']").text
print(successmessag)

Originalmessage = "Success! Thank you! Your order will be delivered in next few weeks :-)."

assert "Success" in successmessag

