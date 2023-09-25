from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import xlrd

from Src.Excel_import_file import row_index

test_data = "../test_data/xlrd_data_driven_data.xls"


driver=webdriver.Chrome(executable_path="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://the-internet.herokuapp.com/login")

with xlrd.open_workbook(filename=test_data) as myworkbook:
    myfile=myworkbook.sheet_by_index(0)
    col=myfile.ncols
    row=myfile.nrows


    for row_index in range(row):
        username=myfile.cell_value(row_index, 0)
        password=myfile.cell_value(row_index, 1)

        driver.find_element(By.ID,value="username").clear()
        driver.find_element(By.ID, value="username").send_keys(username)
        time.sleep(3)

        driver.find_element(By.ID, value="password").clear()
        driver.find_element(By.ID, value="password").send_keys(password)
        time.sleep(3)

    driver.quit()




# @pytest.mark.parametrize("username, password",test_data)
# def test_login(username,password):
#     driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
#
#     driver.get("https://the-internet.herokuapp.com/login")
#     time.sleep(4)
#     driver.find_element(By.ID,value="username").clear()
#     driver.find_element(By.ID,value="username").send_keys(username)
#
#     #PASSWORD
#     time.sleep(4)
#     driver.find_element(By.ID, value="password").clear()
#     driver.find_element(By.ID, value="password").send_keys(password)
#
#     time.sleep(4)




