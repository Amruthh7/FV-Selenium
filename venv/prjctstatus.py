from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path=r"C:\Users\Public\chromedriver\91\chromedriver.exe")
driver.get("https://dev.freshvoice.in")

wait=WebDriverWait(driver,10)
time.sleep(3)

# login as a employee
login = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div/section/div/div/div[2]/div/div/button[1]/span[1]")
login.click()
time.sleep(2)

name = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[1]/div/input")
name.click()
time.sleep(1)
name.send_keys("rajirb777@gmail.com")
time.sleep(1)

password = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[2]/div/input")
password.click()
time.sleep(1)
password.send_keys("Raji@1234")
time.sleep(1)

signin=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[4]/button/span[1]")
signin.click()
time.sleep(2)

status =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/a")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/a")))
status.click()
time.sleep(2)

project =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/div/a[3]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/div/a[3]")))
project.click()
time.sleep(2)

Python = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[1]/div/div[2]/div[3]/div/div/ion-card[1]/ion-card-content/div/div[1]/h2")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[1]/div/div[2]/div[3]/div/div/ion-card[1]/ion-card-content/div/div[1]/h2")))
Python.click()
time.sleep(2)

ViewShortlisted = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[2]/button")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[2]/button")))
ViewShortlisted.click()
time.sleep(2)
