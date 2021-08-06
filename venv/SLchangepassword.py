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
name.send_keys("bharani.rajendran@ekalaiv.com")
time.sleep(1)

password = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[2]/div/input")
password.click()
time.sleep(1)
password.send_keys("Raji@1234")
time.sleep(1)

signin=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[4]/button/span[1]")
signin.click()
time.sleep(3)


wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[7]/ul/li[3]/a")))
ChangePassword = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[7]/ul/li[3]/a")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",ChangePassword)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[7]/ul/li[3]/a")))
ChangePassword.click()
time.sleep(3)


CurrentPassword = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[1]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[1]/div/div/div/input")))
CurrentPassword.click()
time.sleep(3)
CurrentPassword.send_keys("Raji@1234")
time.sleep(2)

NewPassword = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[2]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[2]/div/div/div/input")))
NewPassword.click()
time.sleep(3)
NewPassword.send_keys("Raji@12345")
time.sleep(2)

ChangeNewPassword = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[3]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[2]/div/div[3]/div/div/div/input")))
ChangeNewPassword.click()
time.sleep(2)
ChangeNewPassword.send_keys("Raji@12345")
time.sleep(2)

UpdatePassword = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div/div/div[2]/div/div/ion-card/div[3]/div[2]/button")
UpdatePassword.click()
time.sleep(2)