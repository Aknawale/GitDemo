import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# DATA ENTRY

driver.find_element(By.XPATH,value="//input[@name='name']").send_keys("AKSHAY")
time.sleep(5)

driver.find_element(By.XPATH,value="//input[@name='email']").send_keys("akshaynawale1212@gmail.com")
time.sleep(3)

driver.find_element(By.ID,value="exampleInputPassword1").send_keys("PASSWORD")

driver.find_element(By.ID,value="exampleCheck1").click()

#GENDER

Gen=Select(driver.find_element(By.ID,value="exampleFormControlSelect1"))
Gen.select_by_visible_text("Male")
time.sleep(3)
Gen.select_by_visible_text("Female")

driver.find_element(By.ID,value="inlineRadio1").click()
time.sleep(3)

driver.find_element(By.ID,value="inlineRadio2").click()
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@class='btn btn-success']").click()

driver.execute_script("window.scrollBy(0,-50);")

driver.find_element(By.LINK_TEXT,value="Shop").click()

mobiles=driver.find_elements(By.XPATH,value="//app-card-list/app-card")

for i in mobiles:
    data=i.find_element(By.XPATH,value="div/div/h4/a")
    if(data=="Blackberry"):
        data.find_element(By.XPATH,value="//div/div[2]/button").click()
        time.sleep(5)
    else:
        pass

driver.find_element(By.XPATH,value="//a[@class='nav-link btn btn-primary']").click()

#Checkoutpage

driver.find_element(By.XPATH,value="//button[@class='btn btn-success']").click()
time.sleep(4)

driver.find_element(By.ID,value="country").send_keys("ind")

try:
    #element=WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
    element = WebDriverWait(driver, 25).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    element.click()
except:
    print("The Element is not Available in the search")

driver.find_element(By.XPATH,value="//label[@for='checkbox2']").click()

driver.find_element(By.XPATH,value="//input[@value='Purchase']").click()

successmessage=driver.find_element(By.XPATH,value="//div[@class='alert alert-success alert-dismissible']")

assert "Success" in successmessage.text