from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")


driver.get("https://www.demo.guru99.com/popup.php")

driver.maximize_window()
time.sleep(5)

link_click=driver.find_element(By.LINK_TEXT, value="Click Here").click()

time.sleep(5)
windows = driver.window_handles


for window in windows:
    driver.switch_to.window(window)
    time.sleep(5)
    try:
        driver.find_element(By.NAME, value="emailid").send_keys("Akshaynawale121@gmail.com")
        time.sleep(5)
        driver.find_element(By.NAME, value="btnLogin").click()
    except Exception:
        pass
    driver.close()


driver.quit()

