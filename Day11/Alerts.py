from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://mypage.rediff.com/login/dologin")
# to work with alerts
# driver.find_element(By.XPATH, "//*[@id='pass_div']/input[3]").click()
# time.sleep(10)
# alert=driver.switch_to.alert
# alert.accept()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(10)
windowID=driver.window_handles
parentwindow=windowID[0]
childwindow=windowID[1]
driver.switch_to.window( childwindow)
print(driver.title)
# driver.find_element(By.XPATH,"//input[@name='btn_name']").click()
driver.find_element(By.NAME,"login").send_keys("Swathi")
driver.find_element(By.XPATH,"/html/body/form/center/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/input").click()
driver.switch_to.window(parentwindow)
print(driver.title)















