import time

from selenium import webdriver, Actionchains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = EdgeService("rF:\Selenium_Data\Edge_driver\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.implicitly_wait(15)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.maximize_window()
#
#
# driver.execute_script("window.scrollTo(0, 500);")
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# time.sleep(3)
#
# actions.context_click(driver.find_element(By.ID,"mousehover")).perform()
# time.sleep(3)
#
# actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#
# actions.move_to_element(driver.find_element(By.LINK_TEXT,value="Top")).click().perform()


# driver.get("https://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,value="Click Here").click()
#
#
# windows = driver.window_handles
# for window in windows:
#     driver.switch_to.window(window)
#     try:
#         d= driver.find_element(By.XPATH,value="//h3").text
#         print("The message from text is:-",d)
#     except:
#         pass
# driver.close()
# driver.switch_to.window(windows[0])
# time.sleep(4)

driver.get("https://the-internet.herokuapp.com/frames")

driver.maximize_window()

driver.find_element(By.LINK_TEXT,value="iFrame").click()

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.TAG_NAME,value="p").clear()
time.sleep(3)
driver.find_element(By.TAG_NAME,value="p").send_keys("i AM AJSHAY NAWALE")

time.sleep(4)
