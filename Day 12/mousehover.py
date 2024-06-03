from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
C=driver.find_element(By.XPATH,"//*[@id='global-nav']/nav/div/ul[2]/li[2]/a")
D=driver.find_element(By.XPATH,"//*[@id='global-nav']/nav/div/ul[2]/li[2]/ul/li[5]/a")
act=ActionChains(driver)
act.move_to_element(C).click(D).perform()


