from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
USERNAME = config['ACCOUNT']['Username']
PASSWORD = config['ACCOUNT']['Password']
NAME = config['ACCOUNT']['name']

driver = webdriver.Chrome(executable_path=r'/Users/chenzhenguo/gogolook/chromedriver')


driver.get('https://www.104.com.tw/jobs/main/')

login_button = driver.find_element(By.XPATH, "//a[@href='#' and contains(@onclick, 'login_get()') and contains(@onclick, \"gcn('_login')\") and @onclick=\"login_get();gcn('_login');return false;\"]")


login_button.click()
time.sleep(3)

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

submit_button = driver.find_element(By.ID, "submitBtn")
submit_button.click()

time.sleep(5)

