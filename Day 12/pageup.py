import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(10)
# select single radio button
radiobutton=driver.find_element(By.ID,"female")
driver.execute_script("arguments[0].scrollIntoView();",radiobutton)
radiobutton.click()
driver.save_screenshot("C:\Selenium webdriver\screen.png")
driver.switch_to.new_window('tab')
time.sleep(10)
# radiobutton.click()
# if radiobutton == 'female':
#     radiobutton.click()
#     print(radiobutton)