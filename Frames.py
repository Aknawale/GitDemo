from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://the-internet.herokuapp.com/iframe")

time.sleep(3)

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, value="tinymce")

driver.find_element(By.ID,value="tinymce").clear()

driver.find_element(By.ID,value="tinymce").send_keys("I am updateing the Frames data")

time.sleep(3)

print(driver.find_element(By.XPATH ,value="//p").text)