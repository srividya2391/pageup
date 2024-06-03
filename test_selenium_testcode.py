from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element(By.ID, "id-search-field")
# search_bar.clear()
search_bar.send_keys("hello")
search_bar = driver.find_element(By.ID, "submit")
time.sleep(5)
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
driver.close()