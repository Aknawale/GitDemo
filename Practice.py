from _ast import Assert

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path=r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

#Waits

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element(By.XPATH,value= "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")

time.sleep(2)

fruit_list = []
fruits = driver.find_elements(By.XPATH, value="//div[@class='products']/div")
countt=len(fruits)
print("Count of Fruits is:-", countt)


for j in fruits:
    data = j.find_element(By.XPATH, value="h4").text
    fruit_list.append(data)





print("the list of Fruits is :-", fruit_list)
compare_list=["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]


assert compare_list == fruit_list, "Both strings are matching"



listt = driver.find_elements(By.XPATH, value="//div[@class='products']/div")

count=len(listt)
print("The List has",count," Items")


for i in listt:
    i.find_element(By.XPATH, value="div/button").click()
    time.sleep(5)

driver.find_element(By.XPATH, value= "//img[@src='https://res.cloudinary.com/sivadass/image/upload/v1493548928/icons/bag.png']").click()
time.sleep(5)

driver.find_element(By.XPATH,value= "//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(4)

driver.find_element(By.CLASS_NAME, value="promoCode").send_keys("rahulshettyacademy")
time.sleep(3)

driver.find_element(By.CLASS_NAME, value="promoBtn").click()

#wait = WebDriverWait(driver,15)
#wait.until(EC.presence_of_element_located(By.CLASS_NAME, "promoInfo"))

time.sleep(10)
#Checking of Total Amount or bill



message=driver.find_element(By.CLASS_NAME, value="promoInfo").text

assert message == "Code applied ..!"


values = driver.find_elements(By.CSS_SELECTOR ,"td:nth-child(5) p")
summ=0
for amount in (values):
    summ=summ+int(amount.text)
print("the Total bill is:-", summ)

totall = int(driver.find_element(By.CLASS_NAME,"totAmt").text)

assert summ == totall

#Assignment to check if Code Applied Value is smaller than Total Amount

Discount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
time.sleep(4)
print("the Discounted amount is:-", Discount)

time.sleep(4)
assert Discount < totall










############################################################################33

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.maximize_window()
#
# options = driver.find_elements(By.XPATH,value="//input[@type='checkbox']")
#
# for i in options:
#     if i.get_attribute("value") == ("option2"):
#         i.click()
#         time.sleep(5)
#         assert i.is_selected()
#         break



##Dynamic Dropdown
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# time.sleep(5)
# driver.find_element(By.ID,value="autosuggest").send_keys("Ind")
# time.sleep(5)
# countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
# for i in countries:
#     if (i.text=="India"):
#         i.click()
#         time.sleep(5)
#         break;
#     else:
#         pass
# time.sleep(5)
#
#
#
# assert driver.find_element(By.ID,value="autosuggest").get_attribute("value") == "India"


###########################################################################################3
# driver.get("https://www.demo.guru99.com/popup.php")
#driver.implicitly_wait(50)

# try:
#     element =WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.ID, "Akshay"))).click()
#
# except Exception:
#     print("error for element not found")#driver.implicitly_wait(50)
#
# try:
#     element =WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.ID, "Akshay"))).click()
#
# except Exception:
#     print("error for element not found")

#driver.find_element(By.NAME, value="Akshay_Nawale").click()

# click_link = driver.find_element(By.LINK_TEXT, value="Click Here").click()
# time.sleep(4)
#
#
# windows = driver.window_handles
#
# for window in windows:
#     driver.switch_to.window(window)
#     time.sleep(3)
#     try:
#         driver.find_element(By.NAME,value="emailid").send_keys("ABCCEF")
#         time.sleep(5)
#         driver.find_element(By.NAME, value="btnLogin").click()
#     except Exception:
#         pass
#     driver.close()







#driver.find_element(By.NAME, value="Akshay_Nawale").click()

# click_link = driver.find_element(By.LINK_TEXT, value="Click Here").click()
# time.sleep(4)
#
#
# windows = driver.window_handles
#
# for window in windows:
#     driver.switch_to.window(window)
#     time.sleep(3)
#     try:
#         driver.find_element(By.NAME,value="emailid").send_keys("ABCCEF")
#         time.sleep(5)
#         driver.find_element(By.NAME, value="btnLogin").click()
#     except Exception:
#         pass
#     driver.close()











##################################################################################

# driver.get("https://www.facebook.com/")
#
# driver.maximize_window()
# actions = ActionChains(driver)
#
# username=driver.find_element(By.ID,value="email")
# password = driver.find_element(By.ID, value="pass")
#
# actions.move_to_element(username).click()
# actions.key_down(Keys.SHIFT,username)
# actions.send_keys("Akshaynawalegmail.com")
#
# time.sleep(5)
#
# actions.key_up(Keys.SHIFT,username)
# actions.perform()
# time.sleep(3)
#
# actions.move_to_element(password).click()
# actions.key_down(Keys.SHIFT,password)
# actions.send_keys("Password")
#
# actions.key_up(Keys.SHIFT,password)
#
# time.sleep(5)
#



#################################################################################################


# vacations = driver.find_element(By.LINK_TEXT,value="Home")
# home = driver.find_element(By.LINK_TEXT, value="Vacations")
#
# actions = ActionChains(driver)
# time.sleep(3)
# actions.move_to_element(vacations).perform()
#
# time.sleep(5)
# actions.move_to_element(home).perform()
#
# time.sleep(5)




##############################################################################################3
# Radio1=driver.find_element(By.ID, value="vfb-7-1")
# Radio1.click()
#
# time.sleep(3)
#
# Radio2 = driver.find_element(By.ID,value="vfb-7-2")
# Radio2.click()
#
# time.sleep(3)
#
# Radio3 = driver.find_element(By.ID, value="vfb-7-3")
# Radio3.click()
# time.sleep(3)
#
# Chk1 = driver.find_element(By.ID, value="vfb-6-0")
# Chk1.click()
#
# time.sleep(3)
#
# Chk2 = driver.find_element(By.ID, value="vfb-6-1")
# Chk2.click()
#
# time.sleep(3)
#
# Chk3 = driver.find_element(By.ID,value="vfb-6-2")
#
# if Chk3.is_selected():
#     print("Checkbox 3 is selected")
#
#
#
#
#

##############################################################################################
# country=Select(driver.find_element(By.NAME,value="country"))
#
# country.select_by_visible_text("INDIA")
# time.sleep(4)
#
# country.select_by_visible_text("BAHRAIN")
#
# time.sleep(5)
#
# country.select_by_visible_text("ARGENTINA")
# time.sleep(4)
#
#
# country.select_by_index(1)
#
# time.sleep(4)
#
# country.select_by_index(3)
#
# time.sleep(3)
#
# country.select_by_value("PAKISTAN")
# time.sleep(3)
#
# country.select_by_value("INDIA")
#
#
#
# time.sleep(3)
#
#

#########################################################################################################

# link_1 = driver.find_element(By.XPATH, value="//h3[@class='LC20lb MBeuO DKV0Md']")
# link_1.click()
#
# W3C_link = driver.find_element(By.LINK_TEXT, value="W3C Recommendation")
# W3C_link.click()
#
# # Reverse
#
# driver.back()
#
# time.sleep(5)
#
# driver.forward()
#
# time.sleep(5)
#
# driver.refresh()
#
# time.sleep(5)

#driver.close()