from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
# # find element= xpath is matching with multiple elements
# footer=driver.find_element(By.XPATH,"//footer[@id='u10']//a")
# print(footer.text)
# find elements- with  single matching locator
# driver.get("https://www.facebook.com")
# email=driver.find_elements(By.NAME,"email")
# email[0].send_keys("srividya.23.bca@gmail.com")
# find elements-xpath  is matchingwith multiple elements
# footer=driver.find_elements(By.XPATH, "//footer[@id='u10']//a")
# print(len(footer))
# footer[0].click()
# example for link text
driver.find_element(By.LINK_TEXT,'Careers').click()

