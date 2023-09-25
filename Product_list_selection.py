from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.LINK_TEXT,value="Shop").click()

elements = driver.find_elements(By.XPATH,value="//div[@class='card h-100']")
countt = len(elements)

print("The count is:-", countt)


list=[]
for e in elements:
    data = e.find_element(By.XPATH,"div/h4/a").text
    if(data == "Blackberry"):
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(3)

driver.find_element(By.XPATH,value="//button[@class='btn btn-success']").click()

driver.find_element(By.ID, value="country").send_keys("ind")

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,value="//label[@for='checkbox2']").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,value="btn-success").click()


message = driver.find_element(By.CLASS_NAME,value="alert-success").text

assert "Success!" in message





    # print(data)
    # list.append(data)

# print(list)




