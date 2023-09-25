from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://www.demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME, value="cusid").send_keys("125260")
time.sleep(5)
driver.find_element(By.NAME, value="submit").click()

alerts = driver.switch_to.alert

alerts.message = alerts.text

print("Alert message is:-", alerts.message)

time.sleep(5)
#alerts.accept()
alerts.dismiss()

time.sleep(3)

driver.quit()




