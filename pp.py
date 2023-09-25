from select import select
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.implicitly_wait(10)

checkboxes = driver.find_elements(By.XPATH,value="//input[@type='checkbox']")
print(len(checkboxes))

for i in checkboxes:
    print(i.get_attribute("value"))
    if(i.get_attribute("Value"))=="Option2":
        i.click()
        assert i.is_selected()


Radios=driver.find_elements(By.XPATH,value="//input[@type='radio']")
for j in Radios:
    print(j.text)
for k in Radios:
    print(k.get_attribute("value"))
    if(k.get_attribute("value"))=="radio2":
        k.click()
        time.sleep(4)



#HIDE & SHOW
Element=driver.find_element(By.ID,value="displayed-text")
assert Element.is_displayed()
time.sleep(3)
driver.find_element(By.XPATH,value="//input[@id='hide-textbox']").click()
time.sleep(3)
assert not Element.is_displayed()



# # Radio button
# Radio1=driver.find_element(By.XPATH,value="//input[@value='radio1']").click()
# time.sleep(3)
#
# Radio2=driver.find_element(By.XPATH,value="//input[@value='radio2']").click()
# time.sleep(3)
#
# Radio3=driver.find_element(By.XPATH,value="//input[@value='radio3']").click()
# time.sleep(3)
#
#
# #DROPDOWN
#
# drp=Select(driver.find_element(By.ID,value="dropdown-class-example"))
# drp.select_by_visible_text("Option1")
# time.sleep(3)
# drp.select_by_visible_text("Option3")
# time.sleep(3)
# drp.select_by_visible_text("Option2")
# time.sleep(3)
#
# #Checkbox
#
# driver.find_element(By.ID,value="checkBoxOption1").click()
# time.sleep(3)
#
# driver.find_element(By.ID,value="checkBoxOption2").click()
# time.sleep(3)
#
# driver.find_element(By.ID,value="checkBoxOption3").click()
# time.sleep(3)
#
# #New Window switching
#
# driver.find_element(By.ID,value="openwindow").click()
#
# windows=driver.window_handles
# for window in windows:
#     try:
#         driver.find_element(By.LINK_TEXT,value="Access all our Courses").click()
#         time.sleep(3)
#         driver.close()
#     except:
#         pass
# driver.switch_to.window(windows[0])
#
#
# #Alerts
#
# driver.find_element(By.ID,value="name").send_keys("Akshay Nawale")
# driver.find_element(By.ID,value="alertbtn").click()
# alerts=driver.switch_to.alert
# print(alerts.text)
# alerts.accept()
#
# driver.find_element(By.ID,value="name").send_keys("Accept confirmation")
# driver.find_element(By.ID,value="confirmbtn").click()
# alerts=driver.switch_to.alert
# print(alerts.text)
# alerts.accept()
#
#
# driver.find_element(By.ID,value="name").send_keys("Decline confirmation")
# driver.find_element(By.ID,value="confirmbtn").click()
# alerts=driver.switch_to.alert
# print(alerts.text)
# alerts.dismiss()
#
# driver.find_element(By.ID,value="displayed-text").send_keys("Akshay")
# driver.find_element(By.ID,value="hide-textbox").click()
#
# #MouseHover
#
# actions = ActionChains(driver)
# mousehover = driver.find_element(By.ID,value="mousehover")
# actions.move_to_element(mousehover).perform()
# time.sleep(3)
#
# #NEW TABS
#
# driver.find_element(By.ID,value="opentab").click()
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
# driver.find_element(By.LINK_TEXT,value="Access all our Courses").click()
# time.sleep(4)
# driver.switch_to.window(windows[0])
#
# #Webtable Element
#
# #price
#
# course = driver.find_elements(By.XPATH,value="//fieldset/table/tbody/tr/td[2]")
# price = driver.find_elements(By.XPATH,value="//fieldset/table/tbody/tr/td[3]")
# for i in course:
#     for j in price:
#         print(i.text," ",j.text)
#         break
#
#
# name=driver.find_elements(By.XPATH,value="//div/table/tbody/tr/td[1]")
# position=driver.find_elements(By.XPATH,value="//div/table/tbody/tr/td[2]")
# city = driver.find_elements(By.XPATH,value="//div/table/tbody/tr/td[3]")
#
#
#
#
#


