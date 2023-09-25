from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, value="Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(5)

messagee = driver.find_element(By.XPATH, value="//div[@class='im-para']").text

time.sleep(5)
for i in messagee:
    print(i)

time.sleep(5)


##########################################################################
# driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
# windowsOpened = driver.window_handles
#
# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# driver.find_element(By.ID, "username").send_keys(var)
# driver.find_element(By.ID, "password").send_keys(var)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
#
#
#
# ########################################################
