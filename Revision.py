from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.facebook.com/login/")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.ID, value="email").send_keys("AKSHAYNAWALE")
time.sleep(2)

driver.find_element(By.ID,value="pass").send_keys("PASSWORD")
time.sleep(2)

#window_handle=driver.window_handles()

driver.find_element(By.ID,value="loginbutton").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT,value="Forgotten password?").click()
#
time.sleep(2)
#
driver.save_screenshot("SCREENSHOOT.png")
#
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
#
print("Page Source is:-", driver.page_source)

print("Current URL is:-", driver.current_url)

print("Page Title is:-", driver.title)


#BY ID




#BY CSS SElector
#By X path
#By Name
######################################################################

#By classname

driver.find_element(By.CLASS_NAME,value="inputtext").send_keys("AKSHAY")
time.sleep(10)

#By Tagname

links= driver.find_elements(By.TAG_NAME,value="input")
for i in links:
    print(i)
time.sleep(10)


#################################################
#By Linktext

driver.find_element(By.LINK_TEXT,value="Forgotten account?").click()
time.sleep(3)
driver.back()

##########################################

#by Partial Linktest
driver.find_element(By.PARTIAL_LINK_TEXT,value="Forgotten").click()
time.sleep(3)
driver.back()


#################################################
