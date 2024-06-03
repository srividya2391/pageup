# test cases
# 1.open web browser
# 2.open url www.gmail.com
# 3.enter username
# 4. enter password
# 5. click on login
# 6.capture the tittle of the web page(Actual)
# 7.verify the tittle of the page (Expected)
# 8.close browser
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")
searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium Tutorial - Guru99']").click()
# driver.find_element(By.NAME,"email").send_keys("srividya.bca.23@gmail.com")
# driver.find_element(By.NAME, "pass").send_keys("mypassbpatna23")
# driver.find_element(By.NAME,"login").click()
# act_title=print(driver.title)
# # exp='Facebook – log in or sign up'
driver.close()

