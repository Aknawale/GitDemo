import time
from selenium import Actionchains
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.action_chains import ActionChains




service_obj = Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)


driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(4)

#radio Button

driver.find_element(By.XPATH,value="//input[@value='radio1']").click()
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@value='radio2']").click()
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@value='radio3']").click()
time.sleep(3)

#STATIC DROPDOWN

Dropdown = Select(driver.find_element(By.ID,value="dropdown-class-example"))

Dropdown.select_by_visible_text("Option1")
time.sleep(3)

Dropdown.select_by_value("option1")
time.sleep(4)

Dropdown.select_by_index(2)
time.sleep(5)


#CHECKBOX

driver.find_element(By.ID,value="checkBoxOption1").click()
time.sleep(3)

driver.find_element(By.ID,value="checkBoxOption2").click()
time.sleep(4)

driver.find_element(By.ID,value="checkBoxOption3").click()
time.sleep(4)

#DYNAMIC SEARCHING



driver.find_element(By.ID,value="autocomplete").send_keys("ind")
time.sleep(2)

countries =  driver.find_elements(By.XPATH ,"//ul/li/div")
for i in countries:
    if(i.text=="India"):
        i.click()
    else:
        pass


time.sleep(5)


#Alert
driver.find_element(By.ID,value="alertbtn").click()

alerts = driver.switch_to.alert
time.sleep(3)
alerts.accept()


#TEXT VERIFICATION IN ALERT

driver.find_element(By.ID,value="name").send_keys("akshay")
driver.find_element(By.ID,value="alertbtn").click()
alerts=driver.switch_to.alert

time.sleep(3)
message = alerts.text
print(message)

assert "akshay" in message

alerts.accept()

time.sleep(3)



# HIDE & SHOW

driver.find_element(By.ID,value="show-textbox").click()
time.sleep(3)

driver.find_element(By.ID,value="displayed-text").send_keys("AKSHAY")


#Action Chains

driver.execute_script("window.scrollBy(0,500)")
Actions = ActionChains(driver)
Mouse_hover =  driver.find_element(By.ID,value="mousehover")

Actions.move_to_element(Mouse_hover).perform()
Top = driver.find_element(By.LINK_TEXT,value="Top")
Actions.move_to_element(Top).click().perform()
time.sleep(3)




#Fetching Data from Table

course_list =  driver.find_elements(By.XPATH,value="//div/fieldset/table/tbody/tr/td[3]")

summ=0

for fee in course_list:
    print(fee.text)
    summ=summ+int(fee.text)
print("SUM is:-",summ)



print("Current URL name is:-", driver.current_url)
print("Title of current Tab is:-",driver.title)
print("Page Source is:-",driver.page_source)
driver.back()
time.sleep(4)

driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(4)


driver.save_screenshot("screen.png")



















#TABS SWITCHING
#
# driver.find_element(By.ID,value="opentab").click()
#
# windows=driver.window_handles
#
# for window in windows:
#     driver.switch_to.window(window)
#     time.sleep(3)
#     try:
#         driver.find_element(By.XPATH,value="//button(text()='Access all our Courses')").click()
#
#     except:
#         pass













