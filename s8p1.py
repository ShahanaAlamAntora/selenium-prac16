from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]").click()
driver.implicitly_wait(10)
# No of input boxes present in the web page
inputboxes=driver.find_elements(By.CLASS_NAME,"inputtext")
print(len(inputboxes))
# How to provide value into the text
status=driver.find_element_by_name("firstname").is_displayed()
status2=driver.find_element_by_name("firstname").is_enabled()
status3=driver.find_element_by_name("firstname").is_selected()
print("\nIs displayed or not?")
print("--------------------")
print(status) # True/False
print("\nIs enabled or not?")
print("---------------------")
print(status2)
print("\nIs selected or not?")
print("---------------------")
print(status3)
driver.find_element_by_name("firstname").send_keys("Hamza")
driver.find_element_by_name("lastname").send_keys("Zubair")
driver.find_element_by_name("reg_email__").send_keys("00000000000")
time.sleep(5)
driver.quit()