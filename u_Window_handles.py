from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element(By.LINK_TEXT,value="Click Here").click()
#
# windows= driver.window_handles
# driver.switch_to.window(windows[1])
#
# daata = driver.find_element(By.TAG_NAME,value="h3").text
#
# print(daata)

################# ASSIGNMENTS  #############################

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT,value="Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])


email = driver.find_element(By.XPATH,value="//div/p[2]/strong").text
print(email)
time.sleep(5)


driver.switch_to.window(windows[0])
driver.find_element(By.ID,value="username").send_keys(email)
time.sleep(3)

driver.find_element(By.ID,value="password").send_keys("PASSWORD")
time.sleep(3)

driver.find_element(By.ID,value="terms").click()

time.sleep(3)

driver.find_element(By.ID,value="signInBtn").click()