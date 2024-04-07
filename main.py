from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import json
import time
from todoist_api_python.api import TodoistAPI

file_path = "config.json"

try:
    with open(file_path, "r") as json_file:
        data = json.loads(json_file.read())

    TODOIST_API = data["TODOIST_API"]
    WEB_ADDRESS = data["WEB_ADDRESS"]
    STAFF_EMAIL = data["STAFF_EMAIL"]
    STAFF_PASSWORD = data["STAFF_PASSWORD"]

except FileNotFoundError:
    print("Error: Configuration file 'config.json' not found.")

API = TodoistAPI(TODOIST_API)
TIME_OUT = 60
TAG = " @CS"
PROJECT = " #HOMEWORK"

driver = webdriver.Safari() # change this if u dont use safari
driver.get(WEB_ADDRESS)

login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="x1"]'))
login.send_keys(STAFF_EMAIL, Keys.ENTER)

login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="weblogin_netid"]'))
login.send_keys(STAFF_EMAIL.split('@')[0], Keys.ENTER)

time.sleep(1)
login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="weblogin_password"]'))
login.send_keys(STAFF_PASSWORD, Keys.ENTER)

time.sleep(10)
button = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="trust-browser-button"]'))
button.click()

time.sleep(10)
tasks = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_elements(By.CLASS_NAME,'table-listing-row.lesi-row'))

for task in tasks:
    if ("Closed" not in (task := task.text + TAG + PROJECT)):
        print(task)
        
