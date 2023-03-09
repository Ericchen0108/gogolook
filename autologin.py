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

namelink = driver.find_element(By.ID, "name_link")
namelink.click()
time.sleep(3)

member_center =driver.find_element(By.XPATH, "//a[@href='//pda.104.com.tw']")
member_center.click()
time.sleep(3)

all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])

name_element = driver.find_element(By.XPATH, "//div[contains(@class, 'h2 mb-3')]")
name_element_text = name_element.text.strip()
if name_element == NAME:
    print("名字正確")
else:
    print("名字錯誤")
    
logout_button = driver.find_element(By.XPATH, "//a[@href='//login.104.com.tw/logout']")
logout_button.click()

time.sleep(5)
driver.quit()
