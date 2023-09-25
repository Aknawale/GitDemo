import selenium
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(3)


##########  BY CLASSSSNAME
#driver.find_element(By.CLASS_NAME,value="search-keyword").send_keys("to")
time.sleep(3)

###########************ BYXPATH *************************
#driver.find_element(By.XPATH, value="//input[@placeholder='Search for Vegetables and Fruits']").send_keys("Akshay")
time.sleep(5)


#BY.CSS
driver.find_element(By.CSS_SELECTOR,value="input[placeholder='Search for Vegetables and Fruits']").send_keys("AMAN")
time.sleep(5)


driver.find_element(By.LINK_TEXT,value="Flight Booking").click()
time.sleep(4)

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    time.sleep(4)
    try:
        takeoff=Select(driver.find_element(By.ID,value="ctl00_mainContent_ddl_originStation1_CTXT"))
        takeoff.select_by_visible_text("Shirdi (SAG)")
        time.sleep(3)
    except:
        pass
    driver.close()




#driver.close()
#driver.find_elements(By.XPATH,"//div/div/div[3]/button")
