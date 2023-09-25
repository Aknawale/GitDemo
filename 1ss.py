#AKSHAY APPASAHEB NWALE
#KOPERGAON
#aHEMADNAGAR


from select import select
from selenium import webdriver, Actionchains
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("rF:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# RADIO BUTTON

driver.find_element(By.XPATH,value="//input[@value='radio1']").click()
time.sleep(4)

driver.find_element(By.XPATH,value="//input[@value='radio3']").click()
time.sleep(5)

driver.find_element(By.XPATH,value="//input[@value='radio2']").click()
time.sleep(5)

#SUGGESTION CLASS

# driver.find_element(By.XPATH,value="//input[@id='autocomplete']").send_keys("Ind")


#DROPDOWN
dropdown = Select(driver.find_element(By.ID,value="dropdown-class-example"))
dropdown.select_by_visible_text("Option1")
time.sleep(3)
dropdown.select_by_visible_text("Option3")
time.sleep(5)
dropdown.select_by_visible_text("Option2")
time.sleep(5)


#CHECKBOX

driver.find_element(By.ID,value="checkBoxOption3").click()
time.sleep(3)
driver.find_element(By.ID,value="checkBoxOption1").click()
time.sleep(4)
driver.find_element(By.ID,value="checkBoxOption2").click()
time.sleep(4)


#WINDOW HANDELLING

driver.find_element(By.ID,value="opentab").click()

windows= driver.window_handles

driver.switch_to.window(windows[1])

driver.find_element(By.LINK_TEXT,value="Access all our Courses").click()

driver.switch_to.window(windows[0])
time.sleep(5)

# ALERT EXAMPLE

driver.find_element(By.ID,value="name").send_keys("AKSHAYNAWALE")

driver.find_element(By.ID,value="alertbtn").click()
time.sleep(3)

alerts = driver.switch_to.alert
time.sleep(3)
alerts.accept()

driver.find_element(By.ID,value="confirmbtn").click()

alerts = driver.switch_to.alert
time.sleep(3)
alerts.dismiss()


driver.find_element(By.ID,value="confirmbtn").click()

alerts = driver.switch_to.alert
time.sleep(3)
alerts.accept()


#WEBTABLE EXAMPLE

marks=driver.find_elements(By.XPATH,value="//fieldset/table/tbody/tr/td[3]")
mark_list=[]
for i in marks:
   print(i.text)
   mark_list.append(int(i.text))
print(mark_list)


actions = ActionChains(driver)
actions.move_to_element(By.ID,value="mousehover").perform()





