from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import sys

# Check code format
code = sys.argv[1]

if code.isdigit() and len(code) == 5:
    print("Logging in...")
else:
    print("Code in wrong format (5 digits only)")
    sys.exit()

# Load login details
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DRIVERPATH = os.getenv("DRIVERPATH")

browser_driver = Service(DRIVERPATH)
page = webdriver.Chrome(service=browser_driver)

page.get("https://izone.sunway.edu.my")

username = page.find_element(By.ID, "student_uid")
password = page.find_element(By.ID, "password")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

page.find_element(By.ID, "submit").click()
time.sleep(1)

# Go to iCheckIn page
page.find_element(By.ID, "iCheckInUrl").click()
time.sleep(1)

icheckin = page.find_element(By.ID, "checkin_code")
icheckin.send_keys(code)

time.sleep(1)

page.find_element(By.ID, "iCheckin").click()

time.sleep(3)