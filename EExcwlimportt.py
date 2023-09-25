import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)


file_location = "../test_data/xlrd_data_driven_data.xls"

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

with xlrd.open_workbook(filename=file_location) as my_workbook:
    my_sheet=my_workbook.sheet_by_index(0)

    no_rows = my_sheet.nrows
    no_col = my_sheet.ncols

    for i in range(no_rows):
        username=my_sheet.cell_value(i,0)
        passs = my_sheet.cell_value(i,1)

        driver.find_element(By.ID, value="username").clear()
        driver.find_element(By.ID,value="username").send_keys(username)

        driver.find_element(By.ID, value="password").clear()
        driver.find_element(By.ID,value="password").send_keys(passs)


