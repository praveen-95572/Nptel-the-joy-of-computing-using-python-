from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("W:/Setup/chromedriver_win32/chromedriver")
driver.get("https://web.whatsapp.com/")

wait=WebDriverWait(driver,600)          #wait for 600 time limit

target='"Pinki"'       #enter friend name 
string="Hacker attack  alert! If u create problem then u r in problem to0"           #msg to be send

x_arg = '//span[contains(@title,' + target + ')]'

target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
#target=driver.find_element_by_class("_2MwRD")
target.click()

input_box=driver.find_element_by_class_name("_2A8P4")
for i in range(50):
     input_box.send_keys(string+Keys.ENTER)
     time.sleep(1)
