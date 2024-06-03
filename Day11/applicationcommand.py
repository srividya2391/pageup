from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.get("https://www.google.com")
driver.back() # navigational comments
driver.forward()  # navigational commands
driver.refresh()  # navigational commands
# print(driver.current_url) # application commands
# print(driver.title) # application commands
# print(driver.page_source) # application commands
# email=driver.find_element(By.NAME,"email")
# print(email.is_displayed()) # conditional commands
# print(email.is_enabled()) # conditional commands
# driver.find_element(By.NAME, "pass").send_keys("mypassbpatna23")
# driver.find_element(By.NAME,"login").click()
# act_title=print(driver.title)
# # # exp='Facebook – log in or sign up'
driver.close()
