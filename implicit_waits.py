from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.demo.guru99.com/popup.php")
driver.implicitly_wait(60)
driver.find_element(By.ID, value="AKSHAYYY").click()


driver.quit()