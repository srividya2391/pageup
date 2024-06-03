import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
time.sleep(10)
months="April"
date="20"
years="2025"
#interact with date element with send key method
#driver.find_element(By.ID,"datepicker").send_keys("06/30/2020")
# driver.close()
driver.find_element(By.ID,"datepicker").click()
while True:
 mon=driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
 yr=driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text
 if mon==months and yr==years:
    break
 else:
    driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()
# selecting date
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for a in dates:
    if a.text==date:
        a.click()
        break





