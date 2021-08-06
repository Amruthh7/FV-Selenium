from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains;
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"E:\chromedriver.exe")
driver.get("https://dev.freshvoice.in/")
wait=WebDriverWait(driver,10)
login=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div/section/div/div/div[2]/div/div/button[1]/span[1]")
login.click()
time.sleep(2)

mail = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[1]/div/input")
mail.click()
mail.send_keys("rajirb777@gmail.com")
time.sleep(2)

pwd = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[2]/div/input")
pwd.click()
pwd.send_keys("Raji@12345")

time.sleep(2)

login = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[2]/div/div/div[2]/div/div/div[4]/button/span[1]")
login.click()
time.sleep(2)

status =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/a")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/a")))
status.click()
time.sleep(2)

internship =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/div/a[2]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/div/nav/div/div[1]/div[3]/div/div/a[2]")))
internship.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[1]/div/div[2]/div[3]/div/div/ion-card[1]/ion-card-content/div/div[1]/p[1]")))
internships =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[1]/div/div[2]/div[3]/div/div/ion-card[1]/ion-card-content/div/div[1]/p[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/div[1]/div/div[2]/div[3]/div/div/ion-card[1]/ion-card-content/div/div[1]/p[1]")))
wait=WebDriverWait(driver,30)
internships.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[2]/button")))
viewshortlist =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[2]/button")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[2]/button")))
wait=WebDriverWait(driver,30)
viewshortlist.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")))
back=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")))
wait=WebDriverWait(driver,30)
back.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[3]")))
applicants =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[3]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid/ion-row/ion-col[2]/div/nav/li[3]")))
wait=WebDriverWait(driver,30)
applicants.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")))
back =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/ion-grid/ion-row/ion-col[1]/button/span[1]")))
wait=WebDriverWait(driver,30)
back.click()
time.sleep(2)






