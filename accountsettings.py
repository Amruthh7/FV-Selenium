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

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[4]/ul/li[1]/a")))
accountsettings =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[4]/ul/li[1]/a")
driver.execute_script("arguments[0].scrollIntoView()",accountsettings)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[1]/ion-content/div[1]/div/ion-grid/ion-row/ion-col[2]/div[4]/ul/li[1]/a")))
wait=WebDriverWait(driver,30)
accountsettings.click()
time.sleep(2)

#wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[1]/div/nav/div[2]/div/div/div/div[2]/div[2]/span")))
emailandphonenumber =driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/div[1]/div/div/div[1]/div/nav/div[2]/div/div/div/div[2]/div[2]/span")
#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[1]/div/nav/div[2]/div/div/div/div[2]/div[2]/span")))
emailandphonenumber.click()
time.sleep(2)

editchangemail=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card/div[1]/div[2]/button[2]/span[1]")
editchangemail.click()
time.sleep(2)

password=driver.find_element_by_xpath("/html/body/div[10]/div/div/div[2]/div/div/div/input")
password.click()
time.sleep(2)
password.send_keys("asdfg")
time.sleep(2)

cancel=driver.find_element_by_xpath("/html/body/div[10]/div/div/div[3]/button[1]")
cancel.click()
time.sleep(2)

editphonenumber=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card/div[2]/div[2]/button[2]/span[1]")
editphonenumber.click()
time.sleep(2)

password=driver.find_element_by_xpath("/html/body/div[10]/div/div/div[2]/div/div/div/input")
password.click()
time.sleep(2)
password.send_keys("12345")
time.sleep(2)

cancel=driver.find_element_by_xpath("/html/body/div[10]/div/div/div[3]/button[1]")
cancel.click()
time.sleep(2)

secondarymail=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card/div[4]/div[1]/div/div/input")
secondarymail.send_keys(Keys.CONTROL+"a")
secondarymail.send_keys("aaa@gmail.com")
time.sleep(2)

secondarymobilenumber=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card/div[5]/div[1]/div/input")
secondarymobilenumber.send_keys(Keys.CONTROL+"a")
secondarymobilenumber.send_keys("1234567")
time.sleep(2)

savechanges=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card/div[6]/div[2]/button")
driver.execute_script("arguments[0].scrollIntoView()",savechanges)
time.sleep(2)
savechanges.click()
time.sleep(2)





