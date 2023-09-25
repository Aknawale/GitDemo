import xlrd as xlrd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/login")


with xlrd.open_workbook(filename="../test_data/xlrd_data_driven_data.xls") as my_work_book:

    my_sheet = my_work_book.sheet_by_index(1)


    no_of_col=my_sheet.ncols
    no_of_row=my_sheet.nrows

    for i in range(no_of_row):
        name = my_sheet.cell_value(i,0)
        passs = my_sheet.cell_value(i,1)



