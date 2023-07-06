# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import string, re, requests
from random import choices
from time import sleep
import warnings
import json
warnings.filterwarnings("ignore", category=DeprecationWarning)

BASE_URL = 'https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=it'

class bcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def update_crx():
    crx_page_url = "https://chrome.google.com/webstore/detail/hektcaptcha-hcaptcha-solv/bpfdbfnkjelhloljelooneehdalcmljb" # Replace with the desired Chrome extension URL
    ext_id = crx_page_url.split('/')[-1]
    download_link = f"https://clients2.google.com/service/update2/crx?response=redirect&os=crx&arch=x86-64&nacl_arch=x86-64&prod=chromecrx&prodchannel=unknown&prodversion=88.0.4324.150&acceptformat=crx2,crx3&x=id%3D{ext_id}%26uc"
    with open('solver.crx', 'wb') as file:
        addon_binary = requests.get(download_link).content
        file.write(addon_binary)
    print(f"[*] hcaptcha solver updated {bcolors.MAGENTA}[{bcolors.RESET}{ext_id}{bcolors.MAGENTA}]{bcolors.RESET}")

class RiotGen():
    def __init__(self):
        update_crx()
        options = webdriver.ChromeOptions()
        options.add_extension('solver.crx')
        # self.config             = json.load(open('./config.json'))
        # options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        options.headless        = True
        self.driver             = webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        self.email              = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=6)) + "@gmail.com"
        self.name               = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=7))
        self.password           = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))

    def login(self):
        try:
            self.driver.get(BASE_URL)
            sleep(2)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input', self.email)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input', '01012000')
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/input', self.name)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input').send_keys(self.password)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input', self.password)
            print('[*] solving the hcaptcha')

            # TODO: improve
            not_solved = True
            while not_solved:
                sleep(30)
                try:
                    loding_success = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/svg')
                    not_solved = False
                    print(f'{bcolors.GREEN}[+]{bcolors.RESET}{bcolors.CYAN} Account Created:{bcolors.RESET} {self.name},{self.password}')
                except Exception:
                    print("hcaptcha test failed. Retrying...")
                    next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
                    self.driver.execute_script("arguments[0].click();", next_btn)

            with open('Credentials.txt','a') as handler:
                handler.write(f'{datetime.now()}\n')
                handler.write(f'Email: {self.email}\n')
                handler.write(f'Username: {self.name}\n')
                handler.write(f'Password: {self.password}\n')
                handler.write('---------------------------\n')

        except Exception as e:
            print(f'{bcolors.RED}[-]{bcolors.RESET}{bcolors.CYAN} Failed to Create Account {bcolors.RESET}, reason:', e)

    def insert_field(self, value, arg):
        self.driver.find_element(by=By.XPATH, value=value).send_keys(arg)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)

bot = RiotGen()
bot.login()
