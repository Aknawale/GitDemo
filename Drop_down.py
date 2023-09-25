from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://demo.guru99.com/test/newtours/register.php")

country = Select(driver.find_element(By.NAME, value="country"))

country.select_by_visible_text("INDIA")

time.sleep(5)

country.select_by_visible_text("AMERICAN SAMOA")
time.sleep(5)

country.select_by_visible_text("BAHRAIN")
time.sleep(5)

country.select_by_index(9)
time.sleep(5)


country.select_by_value("CAMBODIA")
time.sleep(5)



driver.get("https://output.jsbin.com/osebed/2")

fruits=Select(driver.find_element(By.ID, value="fruits"))

assert fruits.is_multiple

fruits.select_by_visible_text("Apple")
time.sleep(3)

fruits.deselect_by_visible_text("Apple")
time.sleep(3)

fruits.select_by_index(0)
time.sleep(3)

fruits.select_by_visible_text("Grape")
time.sleep(3)

driver.quit()





