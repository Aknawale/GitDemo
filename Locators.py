from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

# ID, NAME, CLASS NAME, TAGNAME, LINK TEXT, PARTIAL_lINK TEXT, XPATH, CSS SELECTOR
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(3)


#NAME
driver.find_element(By.XPATH,value="//input[@name='name']").send_keys("AKSHAY")
time.sleep(4)


#EMAIL
driver.find_element(By.XPATH,value="//input[@name='email']").send_keys("Nawale@gmail.com")
time.sleep(3)

#PASSWORD
driver.find_element(By.XPATH,value="//input[@type='password']").send_keys("**********Password******")
time.sleep(3)

#Checkbox
driver.find_element(By.XPATH,value="//input[@id='exampleCheck1']").click()
time.sleep(3)

#Dropdown

gen=Select(driver.find_element(By.XPATH,value="//select[@id='exampleFormControlSelect1']"))
gen.select_by_visible_text("Female")
time.sleep(3)


#Two Way Binding
driver.find_element(By.XPATH,value="(//input[@type='text'])[3]").send_keys("************** Two Way Binding reports ***************")

#Employee Status

driver.find_element(By.XPATH,value="//input[@id='inlineRadio2']").click()
time.sleep(4)

driver.find_element(By.XPATH,value="//input[@value='Submit']").click()
time.sleep(3)

messagee = driver.find_element(By.CLASS_NAME, value="alert-success").text
print(messagee)

assert "Success!" in messagee
time.sleep(3)

driver.close()
