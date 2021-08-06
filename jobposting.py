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

wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(text(),'Posting')]")))
posting_dd = driver.find_element_by_xpath("//a[contains(text(),'Posting')]")
posting_dd.click()
time.sleep(2)

Addproject = driver.find_element_by_xpath("//a[contains(text(),'Add Project')]")
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Add Project')]")))
Addproject.click()
time.sleep(2)

projecttitle = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[1]/div/div/div/input")
#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[1]/div/div/div/input")))
time.sleep(2)
projecttitle.click()
time.sleep(2)
projecttitle.send_keys("python")
time.sleep(1)

projectd=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[2]/div[1]/div/div/div/input")
time.sleep(2)
projectd.click()
time.sleep(2)
projectd.send_keys("2 Month")
projectd.send_keys(Keys.ENTER)
time.sleep(2)

projectduration=driver.find_element_by_xpath("/html/body")
#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[3]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[2]/div[1]/div/div/div")))
time.sleep(2)
projectduration.click()
time.sleep(5)

projectduration.send_keys("Free")
projectduration.click()

time.sleep(2)

salary=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[1]/div/div/div")
time.sleep(2)
salary.click()
time.sleep(2)
range=driver.find_element_by_xpath("/html/body/div[8]/div[3]/ul/li[2]")
time.sleep(2)
range.click()

nop=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[2]/div/div/input")
time.sleep(2)
nop.send_keys("2")
nop.click()
time.sleep(2)

projectdescription=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div/div/div/textarea")
time.sleep(2)
projectdescription.send_keys("good project")
projectdescription.click()

previewpost=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")
driver.execute_script("arguments[0].scrollIntoView()",previewpost)
previewpost.click()
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")))
submit=driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")
driver.execute_script("arguments[0].scrollIntoView()",submit)
wait=WebDriverWait(driver,30)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")))
submit.click()
time.sleep(2)