from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)
driver.get('https://itera-qa.azurewebsites.net/home/automation')
# select single check box
# monday=driver.find_element(By.ID,"monday")
# monday.click()
# select multiple checkbox
ch=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]" )
for checkbox in ch:
    if checkbox == "monday" or checkbox == "tuesday":
        checkbox.click()



