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

SearchTalents = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/a")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/a")))
SearchTalents.click()
time.sleep(2)

searchtalents = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/div/a[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[1]/div/div/a[1]")))
searchtalents.click()
time.sleep(2)

MustHave = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/input")))
MustHave.click()
time.sleep(2)
MustHave.send_keys("python")
time.sleep(3)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div[3]/button[1]/span[1] ")))
SEARCH = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div[3]/button[1]/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div[3]/button[1]/span[1]")))
SEARCH.click()
time.sleep(2)

SendMail = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[1]/button/span[1]")
#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[1]/button/span[1]")))
driver.execute_script("arguments[0].scrollIntoView();",SendMail)
SendMail.click()
time.sleep(2)


EMailBox = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[2]/div/p/div/div/textarea")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[8]/div[3]/div/div[2]/div/p/div/div/textarea")))
EMailBox.click()
time.sleep(3)
EMailBox.send_keys("from freshvoice",Keys.ENTER)
time.sleep(3)

SEND = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[3]/button[2]/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[8]/div[3]/div/div[3]/button[2]/span[1]")))
SEND.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[2]/button/span[1]")))
wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[2]/button/span[1]")))
Shortlisted  = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[2]/button/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/div[1]/div/div[3]/div[1]/div[3]/div[3]/div[2]/button/span[1]")))
Shortlisted.click()
time.sleep(2)