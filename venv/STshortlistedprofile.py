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
password.send_keys("Raji@12345")
time.sleep(1)

signin=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[4]/button/span[1]")
signin.click()
time.sleep(2)

wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/a")))
SearchTalents = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/a")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/a")))
SearchTalents.click()
time.sleep(2)

shortlistedprofile = driver.find_element_by_xpath("//a[contains(text(),'Shortlisted Profiles')]")
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Shortlisted Profiles')]")))
shortlistedprofile.click()
time.sleep(3)

sendmail = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/button/span[1]")
driver.execute_script("arguments[0].scrollIntoView();",sendmail)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/button/span[1]")))
sendmail.click()
time.sleep(2)

EmailBox = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[2]/div/p/div/div/textarea")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[8]/div[3]/div/div[2]/div/p/div/div/textarea")))
EmailBox.click()
time.sleep(3)

EmailBox.send_keys("Freshvoice")
time.sleep(2)

SEND = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[3]/button[2]/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[8]/div[3]/div/div[3]/button[2]/span[1]")))
SEND.click()
time.sleep(3)