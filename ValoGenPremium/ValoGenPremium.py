# I uploaded the code of the Premium sice it is slightly faster than thr GUI
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import json
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

all_for_email = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
email = "".join(random.sample(all_for_email, 10)) + '@gmail.com'
username = "".join(random.sample(string.ascii_letters, 8))
all_for_password = all_for_email + string.punctuation
password = "".join(random.sample(all_for_password, 8))

BASE_URL = 'https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=it'

class RiotGen():
    def __init__(self):
        options = Options()
        options.binary_location = r"/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox"
        options.headless = True
        options.add_argument('--window-size=1920,1200')
        DRIVER_PATH = './geckodriver' #full path to geckodriver
        self.driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)
    def login(self):
        extension_path = './noptcha-0.1.8.xpi'
        self.driver.install_addon(extension_path, temporary=True)
        self.driver.get(BASE_URL)
        sleep(2)
        # insert email
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input').send_keys(email)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert date of birth
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input').send_keys('01012000')
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert username
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/input').send_keys(username)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert passoword
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input').send_keys(password)
        # confirm password
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input').send_keys(password)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        print('hCaptcha bypassed!')

bot = RiotGen()
bot.login()

with open('Credentials.txt','a') as handler:
    handler.write(f'{datetime.now()}\n')
    handler.write(f'Email: {email}\n')
    handler.write(f'Username: {username}\n')
    handler.write(f'Password: {password}\n')
    handler.write('---------------------------\n')
