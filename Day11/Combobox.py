from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.find_element(By.LINK_TEXT,"Register").click()
print(driver.title)
driver.find_element(By.NAME,"username").send_keys('swathi')
# select combo box
combobox=driver.find_element(By.TAG_NAME, "select")
combobox.click()
combobox.send_keys("India")
