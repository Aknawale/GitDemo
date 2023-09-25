from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Shop").click()

time.sleep(2)

mobiles = driver.find_elements(By.XPATH,value="//app-card[@class='col-lg-3 col-md-6 mb-3']")
for i in mobiles:
    list=i.find_element(By.XPATH,value="//div/h4/a")
    if (list=="iphone X"):
        driver.find_element(By.XPATH,value="//button[@class='btn btn-info']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//a[@class='nav-link btn btn-primary']").click()
        time.sleep(3)
    else:
        pass
driver.find_element(By.XPATH,value="//button[@class='btn btn-success']").click()
time.sleep(3)

driver.find_element(By.ID,value="country").send_keys("INDIA")
time.sleep(4)
country = Select(driver.find_element(By.ID,value="country"))
country.select_by_visible_text("INDIA")
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@id='checkbox2']").click()
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@value='Purchase']").click()

message = driver.find_element(By.XPATH,value="//div/a")












