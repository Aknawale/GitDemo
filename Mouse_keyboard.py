from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path= r"F:\Selenium_Data\Chrome_driver\chromedriver_win32\chromedriver")

# driver.get("https://demo.guru99.com/test/newtours/")
#
# link_home=driver.find_element(By.LINK_TEXT, value="Home")
# link_vacations=driver.find_element(By.LINK_TEXT, value="Vacations")
#
# actions = ActionChains(driver)
#
# time.sleep(4)
# actions.move_to_element(link_home).perform()
#
# time.sleep(4)
# actions.move_to_element(link_vacations).click()
# actions.perform()



driver.get("https://www.facebook.com/")

actions = ActionChains(driver)
username = driver.find_element(By.ID, value="email")
passs = driver.find_element(By.ID, value="pass")

actions.move_to_element(username)
actions.click(username)
time.sleep(5)

actions.key_down(Keys.SHIFT, username)
actions.send_keys("sharma")

time.sleep(5)

actions.key_up(Keys.SHIFT, username)
time.sleep(5)

actions.move_to_element(username)
actions.click(username)
actions.send_keys("akshayyy")
time.sleep(5)
actions.context_click(username)

time.sleep(5)


actions.move_to_element(passs)
actions.click(passs)
time.sleep(5)
actions.send_keys("Nawale")
time.sleep(5)
actions.perform()

driver.quit()

