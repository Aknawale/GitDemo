import pytest
import xlrd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

file_location = "../test_data/xlrd_data_driven_data.xls"

driver = webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

driver.get("https://the-internet.herokuapp.com/login")

with xlrd.open_workbook(filename=file_location) as my_work_book:
    my_file = my_work_book.sheet_by_index(0)
    no_cols = my_file.ncols
    no_rows = my_file.nrows

    for row_index in range(no_rows):
        username = my_file.cell_value(row_index, 0)
        password = my_file.cell_value(row_index, 1)

        driver.find_element(By.ID, value="username").clear()
        driver.find_element(By.ID, value="username").send_keys(username)
        time.sleep(5)
        driver.find_element(By.ID, value="password").clear()
        driver.find_element(By.ID, value="password").send_keys(password)
        time.sleep(5)

driver.quit()


