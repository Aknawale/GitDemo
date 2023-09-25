import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

#RADIO BUTTON
driver.find_element(By.XPATH,value="//input[@value='radio1']").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,value="input[value='radio2']").click()
time.sleep(3)

driver.find_element(By.XPATH,value="//input[@value='radio3']")
time.sleep(4)

#DYNAMIC SELECTION
driver.find_element(By.ID,value="autocomplete").send_keys("ind")
time.sleep(2)

countries =  driver.find_elements(By.XPATH ,"//ul/li/div")
for i in countries:
    if(i.text=="India"):
        i.click()
    else:
        pass


time.sleep(5)

# country= Select(driver.find_element(By.ID,value="autocomplete")).send_keys("Ind")
# time.sleep(3)
# country.select_by_visible_text("India")

#DROP DOWN

driver.find_element(By.ID,value="dropdown-class-example").click()
driver.find_element(By.XPATH,value="//option[@value='option1']").click()
time.sleep(3)

driver.find_element(By.ID,value="dropdown-class-example").click()
driver.find_element(By.XPATH,value="//option[@value='option2']").click()
time.sleep(3)

driver.find_element(By.ID,value="dropdown-class-example").click()
driver.find_element(By.XPATH,value="//option[@value='option3']").click()
time.sleep(3)


#CHECKBOX

driver.find_element(By.ID,value="checkBoxOption1").click()
time.sleep(4)

driver.find_element(By.ID,value="checkBoxOption2").click()
time.sleep(4)

driver.find_element(By.ID,value="checkBoxOption3").click()
time.sleep(4)


#TAB SWITCHING

driver.find_element(By.ID,value="opentab").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])
time.sleep(3)
driver.find_element(By.LINK_TEXT,value="Contact").click()
driver.close()

driver.switch_to.window(windows[0])

driver.find_element(By.ID,value="name").send_keys("AKSHAY APPASAHEB NAWALE")
driver.find_element(By.ID,value="alertbtn").click()

alerts = driver.switch_to.alert

message = alerts.text
print(message)

assert "AKSHAY" in message
time.sleep(3)
alerts.accept()

driver.find_element(By.ID,value="name").send_keys("AKSHAY APPASAHEB NAWALE")
driver.find_element(By.ID,value="confirmbtn").click()

alerts = driver.switch_to.alert
alerts.dismiss()

driver.execute_script("window.scrollTo(0,400)")
prices = driver.find_elements(By.XPATH,value="//fieldset/table/tbody/tr/td[3]")
summ=0
for i in prices:
    summ=summ+int(i.text)
print("Sum is:-",summ)

names =  driver.find_elements(By.XPATH,value="//table/tbody/tr/td[1]")
print("The names of employee are:-", names)

amount = driver.find_elements(By.XPATH,value="//table/tbody/tr/td[4]")
Totall_amount=0
for j in amount:
    Totall_amount= Totall_amount + int(j.text)

print("The Total amount is:-", Totall_amount)