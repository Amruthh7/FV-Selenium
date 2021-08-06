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

address=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/div[1]/div/div/div[1]/div/nav/div[2]/div/div/div/div[3]")
address.click()
time.sleep(2)

address1=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[2]/div/div/div/input")
address1.click()
time.sleep(2)
address1.send_keys(Keys.CONTROL+"a")
address1.send_keys("assd")
time.sleep(2)

address2=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[3]/div/div/div/input")
address2.click()
time.sleep(2)
address2.send_keys(Keys.CONTROL+"a")
address2.send_keys("assdefr")
time.sleep(2)

address3=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[4]/div/div/div/input")
address3.click()
time.sleep(2)
address3.send_keys(Keys.CONTROL+"a")
address3.send_keys("assdfred")
time.sleep(2)

country=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[5]/div[1]/div/div/div/input")
country.click()
time.sleep(2)
country.send_keys(Keys.CONTROL+"a")
country.send_keys("India")
country.send_keys(Keys.ENTER)
time.sleep(2)

state=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[5]/div[2]/div/div/div/input")
state.click()
time.sleep(2)
state.send_keys(Keys.CONTROL+"a")
state.send_keys("Tamil Nadu")
state.send_keys(Keys.ENTER)
time.sleep(2)

city=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[6]/div[1]/div/div/div/input")
address3.click()
time.sleep(2)
city.send_keys(Keys.CONTROL+"a")
city.send_keys("Trichy")
time.sleep(2)

pincode=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/ion-card[1]/div[6]/div[2]/div/div/input")
address3.click()
time.sleep(2)
pincode.send_keys(Keys.CONTROL+"a")
pincode.send_keys("620008")
time.sleep(2)

savechanges=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[4]/ion-content/div[1]/div/div/div[2]/div/div/div/div/div[2]/button/span[1]")
driver.execute_script("arguments[0].scrollIntoView()",savechanges)
time.sleep(2)
savechanges.click()
time.sleep(2)









