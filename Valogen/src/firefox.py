from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from random import choices
from time import sleep
import warnings
import json
import os
warnings.filterwarnings("ignore", category=DeprecationWarning)

from .names import generate_name

BASE_URL = 'https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=en'

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

def update_xpi():
    owner = "Wikidepia"
    repo = "hektCaptcha-extension"
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    releases = requests.get(api_url).json()
    for release in releases:
        if not release['prerelease']:
            tag_name = release["tag_name"]
            download_url = f"https://github.com/{owner}/{repo}/releases/download/{tag_name}/hektCaptcha-{tag_name}.firefox.xpi"
            with open("solver.xpi", "wb") as file:
                file.write(requests.get(download_url).content)
            print(f"[*] hcaptcha solver updated {bcolors.MAGENTA}[{bcolors.RESET}{tag_name}{bcolors.MAGENTA}]{bcolors.RESET}")
            break
        
class RiotGen():
    def __init__(self):
        update_xpi()
        self.config = json.load(open('src/config.json'))
        options = Options()
        # options.binary_location  = self.config["firefox_binary_location"]
        options.headless         = False
        self.driver              = webdriver.Firefox(options, service=FirefoxService(GeckoDriverManager().install())) # log_path='/dev/null'
        self.email               = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=6)) + "@randommail.com"
        self.name                = generate_name()
        self.password            = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))

    def login(self):
        try:
            extension_path = './solver.xpi'
            self.driver.install_addon(extension_path, temporary=True)
            self.driver.get(BASE_URL)
            sleep(2)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input', self.email)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input', '01012000')
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/input', self.name)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input').send_keys(self.password)
            self.insert_field('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input', self.password)
            print('[*] solving the hcaptcha')
            
            not_solved = True
            while not_solved:
                try:
                    if self.driver.current_url != BASE_URL:
                        # print(f'{bcolors.GREEN}[+]{bcolors.RESET}{bcolors.CYAN} Account Created:{bcolors.RESET} {self.name},{self.password}')
                        return self.email, self.name, self.password
                except Exception:
                    print("hcaptcha test failed. Retrying...")
                    next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
                    self.driver.execute_script("arguments[0].click();", next_btn)

        except Exception as e:
            print(f'{bcolors.RED}[-]{bcolors.RESET}{bcolors.CYAN} Failed to Create Account {bcolors.RESET}, reason:', e)
            return None, None, None

    def insert_field(self, value, arg):
        self.driver.find_element(by=By.XPATH, value=value).send_keys(arg)
        next_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button')
        self.driver.execute_script("arguments[0].click();", next_btn)

# bot = RiotGen()
# bot.login()
