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
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(text(),'Posting')]")))
posting_dd = driver.find_element_by_xpath("//a[contains(text(),'Posting')]")
posting_dd.click()
time.sleep(2)

Addinternship = driver.find_element_by_xpath("//a[contains(text(),'Add Internship')]")
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Add Internship')]")))
Addinternship.click()
time.sleep(2)

Intenshiptitle = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[1]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[1]/div/div/div/input")))
Intenshiptitle.click()
time.sleep(2)
Intenshiptitle.send_keys("python")
time.sleep(1)


AddLocations = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[2]/div[1]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[1]/div/div/div/input")))
AddLocations.click()
time.sleep(2)

AddLocations.send_keys("coimbatore",Keys.ENTER)
time.sleep(2)


InternshipDuration = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[2]/div[2]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[2]/div[2]/div/div/div/input")))
InternshipDuration.click()
time.sleep(2)

InternshipDuration.send_keys("2 Month",Keys.ARROW_DOWN,Keys.ENTER)

time.sleep(2)

Internship = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[1]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[1]/div/div/div/input")))
Internship.click()
time.sleep(2)

Internship.send_keys("Remote",Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(2)

InternshipType = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[2]/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[2]/div/div/div/input")))
InternshipType.click()
time.sleep(2)

InternshipType.send_keys("Without Stipend",Keys.ARROW_DOWN,Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[3]/div[2]/div/div/div/input")))
time.sleep(3)

Numberofposition = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div[2]/div[1]/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div[2]/div[1]/div/input")))
Numberofposition.click()
time.sleep(2)

Numberofposition.send_keys("3",Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(2)

Marks = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div[2]/div[2]/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div[2]/div[2]/div/div/input")))
Marks.click()
time.sleep(2)

Marks.send_keys("70 to 80",Keys.ARROW_DOWN,Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[4]/div[2]/div[2]/div/div/input")))
time.sleep(3)



wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[5]/div/div/div/textarea")))
JobDetails = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[5]/div/div/div/textarea")
driver.execute_script("arguments[0].scrollIntoView();",JobDetails)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[5]/div/div/div/textarea")))
JobDetails.click()
time.sleep(3)

JobDetails.send_keys("from freshvoice")
time.sleep(3)


Prerequisites = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[7]/div/div/div/div/input")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[7]/div/div/div/div/input")))
Prerequisites.click()
time.sleep(2)

Prerequisites.send_keys("PHP",Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-grid[1]/ion-row/ion-col[1]/div/div/div/div[7]/div/div/div/div/input")))
time.sleep(2)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")))
PREVIEWPOST = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")))
PREVIEWPOST.click()
time.sleep(2)

SUBMIT = driver.find_element_by_xpath("/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/ion-app/ion-split-pane/ion-router-outlet/div[2]/ion-content/ion-footer/ion-toolbar/div/ion-button[2]")))
SUBMIT.click()
time.sleep(2)












