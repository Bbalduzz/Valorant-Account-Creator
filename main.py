import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# import progressbar

BASE_URL = 'https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=it'

print('>> Creating crediantials...', end=' ')
all_for_email = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
all_for_password = all_for_email + string.punctuation
email = "".join(random.sample(all_for_email, 10)) + '@gmail.com'
username = "".join(random.sample(string.ascii_letters, 8))
password = "".join(random.sample(all_for_password, 8))
print('DONE')

# def animated_marker():
#     widgets = ['>> Creating Account: ',progressbar.AnimatedMarker()]
#     bar = progressbar.ProgressBar(widgets=widgets).start()   
#     for i in range(150):
#         time.sleep(0.1)
#         bar.update(i)

# print(animated_marker())

print('>> Creating Account...', end=' ')
class RiotGen():
    def __init__(self):
        options = Options()
        options.binary_location = r"/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox" # <== change to your browser binary location
        # options.headless = True
        options.add_argument('--window-size=1920,1200')
        DRIVER_PATH = '/Users/edoardo/Documents/projects/ValorantAccountGenerator/geckodriver' # <== change to the path with the projects (ex. /Downloads//ValorantAccountGenerator/geckodriver)
        self.driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)
    def login(self):
        self.driver.get(BASE_URL)
        sleep(2)
        # insert email
        email_in = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input')
        email_in.send_keys(email)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert date of birth
        birth_in = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input')
        birth_in.send_keys('01012000')
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert username
        username_in = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/input')
        username_in.send_keys(username)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        # insert passoword
        password_in = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input')
        password_in.send_keys(password)
        # confirm password
        confirm_password_in = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input')
        confirm_password_in.send_keys(password)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)

        print('COMPLETE THE hCaptcha TEST')

bot = RiotGen()
bot.login()
with open('Credentials.txt','a') as handler:
    handler.write(f'{datetime.now()}\n')
    handler.write(f'Email: {email}\n')
    handler.write(f'Username: {username}\n')
    handler.write(f'Password: {password}\n')
    handler.write('---------------------------\n')
    





