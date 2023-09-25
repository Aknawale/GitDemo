import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="r F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver.implicitly_wait(10)
# driver.get("https://rahulshettyacademy.com/angularpractice/shop")
#
# driver.find_element(By.LINK_TEXT,value="Home").click()
#
# driver.find_element(By.XPATH,value="//input[@name='name']").send_keys("AKSHAYYYY")
#
# driver.find_element(By.CSS_SELECTOR,value="input[name='email']").send_keys("akshaynawale121@gmail.com")
#
# driver.find_element(By.ID,value="exampleInputPassword1").send_keys("password")
#
# driver.find_element(By.ID,value="exampleCheck1").click()
#
# gender=Select(driver.find_element(By.ID,value="exampleFormControlSelect1"))
# gender.select_by_visible_text("Female")
#
# driver.refresh()
#
# driver.back()
# driver.forward()
#
#
# #driver.save_screenshot("AA.png")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

Actions= ActionChains(driver)
option1=driver.find_element(By.XPATH, value= "//img[@alt='Brocolli - 1 Kg']")
Actions.move_to_element(option1).perform()
time.sleep(3)

driver.find_element(By.LINK_TEXT,value="Top Deals").click()
windows =driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    time.sleep(4)
    try:
        driver.find_element(By.ID,value="search-field").send_keys("Akshay")
    except:
        pass
    driver.close()













