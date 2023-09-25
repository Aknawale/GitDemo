from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.moneycontrol.com/")

print("Page Source is:- ", driver.page_source)

time.sleep(5)
print("Page Title is:- ", driver.title)

time.sleep(5)
print("Current URL is:- ", driver.current_url)

time.sleep(5)


driver.quit()