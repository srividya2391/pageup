import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get('https://itera-qa.azurewebsites.net/home/automation')
time.sleep(10)
# select single radio button
radiobutton=driver.find_element(By.ID,"female")
# radiobutton.click()
if radiobutton == 'female':
    radiobutton.click()
    print(radiobutton)

# select muttipl