from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path=r"C:\Users\Public\chromedriver\91\chromedriver.exe")
driver.get("http://localhost:3000/")

a=driver.find_element_by_xpath("/html/body/div/div/div/p[1]")
a.click()
time.sleep(2)

next=driver.find_element_by_xpath("/html/body/div/div/div/button")
next.click()
time.sleep(2)

b=driver.find_element_by_xpath("/html/body/div/div/div/p[3]")
b.click()
time.sleep(2)

next=driver.find_element_by_xpath("/html/body/div/div/div/button")
next.click()
time.sleep(2)


c=driver.find_element_by_xpath("/html/body/div/div/div/p[2]")
c.click()
time.sleep(2)

next=driver.find_element_by_xpath("/html/body/div/div/div/button")
next.click()
time.sleep(2)

d=driver.find_element_by_xpath("/html/body/div/div/div/p[1]")
d.click()
time.sleep(2)

next=driver.find_element_by_xpath("/html/body/div/div/div/button")
next.click()
time.sleep(2)

e=driver.find_element_by_xpath("/html/body/div/div/div/p[2]")
e.click()
time.sleep(2)

finish=driver.find_element_by_xpath("/html/body/div/div/div/button")
finish.click()
time.sleep(2)