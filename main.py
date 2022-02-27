from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ACCOUNT_EMAIL = os.environ.get("YOUR_ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("YOUR_ACCOUNT_PASSWORD")

chrome_driver_path = os.environ.get("YOUR_CHROME_DRIVER_PATH")
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.linkedin.com/login/de?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


# Accepting the cookies
accept_cookies = driver.find_element(By.XPATH, "//*[@id='artdeco-global-alert-container']/div/section/div/div[2]/button[2]")

email_input: WebElement = driver.find_element(By.ID, "username")
password_input: WebElement = driver.find_element(By.ID, "password")
login_button: WebElement = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")


email_input.send_keys(ACCOUNT_EMAIL)
password_input.send_keys(ACCOUNT_PASSWORD)
login_button.send_keys(Keys.ENTER)

time.sleep(5)

# after getting logged in, search for the job
jobs_link: WebElement = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_link.click()

time.sleep(2)

first_job: WebElement = driver.find_element(By.XPATH, "//*[@id='ember251']")
first_job.click()
time.sleep(2)

easy_apply_btn: WebElement = driver.find_element(By.XPATH, "//*[@id='ember518']")
easy_apply_btn.click()
time.sleep(2)

