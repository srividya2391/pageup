import exceptiongroup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
# driver.implicitly_wait(10) # implicit wait
mywait=WebDriverWait(driver,10) # explicit wait declration
driver.get("https://www.facebook.com")
email=mywait.until(EC.presence_of_element_located((By.NAME,"email")))
# email=driver.find_element(By.NAME,"email")
email.send_keys("srividya.bca.23@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("mypassbpatna23")
driver.find_element(By.NAME,"login").click()
act_title=print(driver.title)
# # # exp='Facebook – log in or sign up'
driver.close()
