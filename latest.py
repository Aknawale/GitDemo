import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)


file_location = "../test_data/xlrd_data_driven_data.xls"

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(10)