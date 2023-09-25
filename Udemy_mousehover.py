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

actions = ActionChains(driver)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
actions.move_to_element(driver.find_element(By.ID,value="mousehover")).perform()
time.sleep(4)

#actions.move_to_element(driver.find_element(By.LINK_TEXT,value="Top")).click().perform()
time.sleep(3)
actions.move_to_element(driver.find_element(By.ID,value="checkBoxOption1")).click().perform()
time.sleep(3)
actions.double_click(driver.find_element(By.ID,value="checkBoxOption1")).click().perform()
time.sleep(3)



driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(4)
driver.find_element(By.LINK_TEXT,value="Click Here").click()

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    try:
        mess=driver.find_element(By.TAG_NAME,value="h3")
        time.sleep(3)
        print(mess.text)
    except:
        pass

    

time.sleep(3)