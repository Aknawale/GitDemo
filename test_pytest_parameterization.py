import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

test_data = [["user1", "password1"], ["user2", "password2"],]


@pytest.mark.parametrize("username, password", test_data)
def test_login(username, password):
    driver = webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(5)
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(5)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(3)
    driver.quit()
