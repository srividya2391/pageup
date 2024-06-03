import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(100)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.LINK_TEXT,"Redmi 12C (Mint Green, 4GB RAM, 64GB Storage) | High Performance Mediatek Helio G85 | Big 17cm(6.71) HD+ Display with 5000mAh(typ) Battery").click()
windowID=driver.window_handles
parentwindow=windowID[0]
childwindow=windowID[1]
driver.switch_to.window(childwindow)
time.sleep(10)
cart=driver.find_element(By.XPATH,"//input[@name='submit.add-to-cart']")
driver.execute_script("arguments[0].scrollIntoView();",cart)
cart.click()
driver.close()


##########
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver= webdriver.Chrome()
# driver.get("https://dev2.printme.com/")
# driver.find_element(By.ID,"navbarDropdown1").click()
# time.sleep(10)
# 2nd program remove duplicate char
# a="srividya"
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
# print(b)
# 3rd program
# a="abc"
# b="xyz"
# temp=b
# b=a
# a=temp
# print("a is =",a)
# print("b is =",b)
#4th program
a="nayana"
b=""
for i in a:
    b=i+b
if(b==a):
    print(b)
else:
    print("not a palindrome")









