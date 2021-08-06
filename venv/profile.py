from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains;
driver=webdriver.Chrome(executable_path=r"C:\Users\Public\chromedriver\91\chromedriver.exe")
driver.get("https://dev.freshvoice.in")

wait=WebDriverWait(driver,10)
time.sleep(3)

# login as a jobseeker
login = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div/section/div/div/div[2]/div/div/button[1]/span[1]")
login.click()
time.sleep(2)

name = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[1]/div/input")
name.click()
time.sleep(1)
name.send_keys("amruthh.3@gmail.com")
time.sleep(1)

password = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[2]/div/input")
password.click()
time.sleep(1)
password.send_keys("!Amruth12345%")
time.sleep(1)

signin=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[4]/button/span[1]")
signin.click()
time.sleep(2)

profile = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/a[2]/span")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/a[2]/span")))
profile.click()
time.sleep(2)

edit=driver.find_element_by_xpath("//*[@id='blue_btn']/span[1]")
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='blue_btn']/span[1]")))
edit.click()
time.sleep(2)



AddAchivements=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/div[19]/button/span[1]")
driver.execute_script("arguments[0].scrollIntoView();",AddAchivements)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/div[19]/button/span[1]")))
AddAchivements.click()
time.sleep(2)

enterAchivementTitle=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ul[1]/li[1]/div[2]/div/div[1]/div[1]/ion-input/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ul[1]/li[1]/div[2]/div/div[1]/div[1]/ion-input/input")))
time.sleep(2)
enterAchivementTitle.send_keys("abc")
time.sleep(2)




