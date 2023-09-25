from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.moneycontrol.com/stocks/marketstats/bseloser/index.php")

time.sleep(3)

#driver.save_screenshot("abc.png")

driver.save_screenshot("../Images/abc.png")

time.sleep(3)

driver.quit()