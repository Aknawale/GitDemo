from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://demo.guru99.com/test/radio.html")

#radio1 = driver.find_element(By.ID, value="vfb-7-1")
radio1=driver.find_element(By.XPATH, value="//input[@value='Option 1']")
radio1.click()

time.sleep(5)

radio2 = driver.find_element(By.ID, value="vfb-7-2")
radio2.click()

time.sleep(5)

radio3 = driver.find_element(By.ID, value="vfb-7-3")
radio3.click()

time.sleep(5)

if radio1.is_selected():
    print("Radio1 is selected")

elif radio2.is_selected():
    print("radio2 is selected")

else:
    print("Radio 3 is selected")

#Checkbox collection

chk1 = driver.find_element(By.ID, value="vfb-6-0")
chk1.click()

time.sleep(5)

chk2 = driver.find_element(By.ID, value="vfb-6-1")
chk2.click()

time.sleep(5)

chk3 = driver.find_element(By.ID, value="vfb-6-2")
chk3.click()

time.sleep(5)


driver.quit()





