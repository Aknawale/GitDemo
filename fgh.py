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

#service_obj=Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
#driver=webdriver.Chrome(service=service_obj)
driver_path ="rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver"
service_obj = EdgeService(driver_path)

# Create a WebDriver instance for Microsoft Edge
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

time.sleep(3)


Radio1=driver.find_element(By.XPATH,value="//input[@value='radio1']")
Radio1.click()

time.sleep(3)

Radio2=driver.find_element(By.XPATH,value="//input[@value='radio2']")
Radio2.click()
time.sleep(3)

Radio3=driver.find_element(By.XPATH,value="//input[@value='radio3']")
Radio3.click()
time.sleep(3)

#Suggestion Class

driver.find_element(By.ID,value="autocomplete").send_keys("ind")
time.sleep(3)

eee=driver.find_elements(By.XPATH,value="//li/div")
for i in eee:
    if(i.text=="India"):
        i.click()
    else:
        pass
# ele=Select(driver.find_element(By.ID,value="autocomplete"))
# time.sleep(3)
# ele.select_by_visible_text("India")

#DROPDOWN

drp=Select(driver.find_element(By.ID,value="dropdown-class-example"))

drp.select_by_visible_text("Option1")
time.sleep(3)
drp.select_by_visible_text("Option2")
time.sleep(4)
drp.select_by_visible_text("Option3")
time.sleep(4)



#CHECKBOX

driver.find_element(By.ID,value="checkBoxOption1").click()

time.sleep(3)

driver.find_element(By.ID,value="checkBoxOption2").click()
time.sleep(3)

driver.find_element(By.ID,value="checkBoxOption3").click()
time.sleep(3)

# SWITCH TO WINDIW

driver.find_element(By.ID,value="openwindow").click()
wind=driver.window_handles
for w in wind:
    driver.switch_to.window(w)
    time.sleep(3)
    try:
        driver.find_element(By.LINK_TEXT,value="Access all our Courses").click()
    except:
        pass
driver.close()

#driver.switch_to.default_content()
driver.switch_to.window(wind[0])

driver.find_element(By.ID,value="opentab").click()
time.sleep(3)

windows = driver.window_handles

for i in windows:
    driver.switch_to.window(i)
    #driver.switch_to.window(i):
    try:
        driver.find_element(By.LINK_TEXT, value="Access all our Courses").click()
    except:
        pass


driver.switch_to.window(windows[0])

driver.find_element(By.ID,value="name").send_keys("Akshay")
driver.find_element(By.ID,value="alertbtn").click()

alerts = driver.switch_to.alert

print(alerts.text)
message = alerts.text
assert "Akshay" in message
alerts.accept()

driver.find_element(By.ID,value="name").send_keys("Akshay")
driver.find_element(By.ID,value="confirmbtn").click()

alerts = driver.switch_to.alert
print(alerts.text)
message1=alerts.text

assert "Akshay" in message1
alerts.dismiss()


#Web Table Example

courses = driver.find_elements(By.XPATH,value="//fieldset/table/tbody[1]/tr/td[2]")
for i in courses:
    print(i.text)

marks = driver.find_elements(By.XPATH,value="//fieldset/table/tbody[1]/tr/td[3]")
Total=0
for i in marks:
    print(i.text)
    Total=Total+int(i.text)
print("Total AMount is:- ", Total)
for i in courses:
    for j in marks:
        print(i.text,j.text)
        break

Actions=ActionChains(driver)
Actions.move_to_element(By.ID,value="mousehover")
time.sleep(10)

driver.find_element(By.ID,value="mousehover")
# driver.find_element(By.ID,value="dropdown-class-example").click()
# driver.find_element(By.XPATH,value="//option[@value='option1']").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH,value="//option[@value='option2']").click()
# time.sleep(3)
#
#
# driver.find_element(By.XPATH,value="//option[@value='option3']").click()
# time.sleep(3)






