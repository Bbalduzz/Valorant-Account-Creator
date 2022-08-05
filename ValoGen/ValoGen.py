# == this is not the Premium version ==
# If u want to see the premium version join my ds: https://discord.gg/6AEdmkXUbS
from pathlib import Path
from tkinter import *
import pyperclip as pc
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import json


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_email(entry):
    all_for_email = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
    email = "".join(random.sample(all_for_email, 10)) + '@gmail.com'
    entry.delete(0, END)
    entry.insert(0, email)
def generate_username(entry):
    username = "".join(random.sample(string.ascii_letters, 8))
    entry.delete(0, END)
    entry.insert(0, username)
def generate_password(entry):
    all_for_email = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
    all_for_password = all_for_email + string.punctuation
    password = "".join(random.sample(all_for_password, 8))
    entry.delete(0, END)
    entry.insert(0, password)

window = Tk()
window.iconbitmap("assets/ValoGen.ico")
window.title('ValoGen | Valorant Account Generator')
window.geometry("580x324")
window.configure(bg = "#232429")

canvas = Canvas(
    window,
    bg = "#232429",
    height = 324,
    width = 580,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
passaword_area_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
passaword_area_bg_1 = canvas.create_image(
    400.0,
    241.0,
    image=passaword_area_image_1
)
password_area = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
)
password_area.place(
    x=326.0,
    y=225.0,
    width=148.0,
    height=30.0
)

username_area_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
username_area_bg_2 = canvas.create_image(
    400.0,
    172.0,
    image=username_area_image_2
)
username_area = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
)
username_area.place(
    x=326.0,
    y=157.0,
    width=148.0,
    height=28.0
)

email_area_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
email_area_bg_3 = canvas.create_image(
    400.0,
    104.5,
    image=email_area_image_3
)
email_area = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
)
email_area.place(
    x=326.0,
    y=89.0,
    width=148.0,
    height=29.0
)

def ValoGen():
    email = email_area.get()
    username = username_area.get()
    password = password_area.get()
    BASE_URL = 'https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=it'
    class RiotGen():
        def __init__(self):
            options = Options()
            # options.binary_location = r"C:/Program Files/Firefox Developer Edition/firefox.exe" # <== change to your browser binary location
            # options.headless = True
            options.add_argument('--window-size=1920,1200')
            DRIVER_PATH = 'E:/vscode_projects/python/ValGen/ValoGen/geckodriver.exe' # <== change to the path with the projects (ex. /Downloads//ValorantAccountGenerator/geckodriver)
            self.driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)
        def login(self):
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
    
    bot = RiotGen()
    bot.login()
    print('complete the reCaptcha test')
    
    with open('Credentials.txt','a') as handler:
        handler.write(f'{datetime.now()}\n')
        handler.write(f'Email: {email}\n')
        handler.write(f'Username: {username}\n')
        handler.write(f'Password: {password}\n')
        handler.write('---------------------------\n')

    def write_json(new_data, filename='accounts.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['accounts_details'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    
    account = {
        'creation': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'email': email,
        'username': username,
        'password': password,
    }
    write_json(account)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [generate_email(email_area),generate_username(username_area),generate_password(password_area), ValoGen()],
    relief="flat"
)
button_1.place(
    x=77.0,
    y=157.0,
    width=120.0,
    height=40.0
)

canvas.create_text(
    321.0,
    69.0,
    anchor="nw",
    text="email",
    fill="#787B8A",
    font=("Poppins ExtraBold", 14 * -1)
)

canvas.create_text(
    321.0,
    200.0,
    anchor="nw",
    text="password",
    fill="#787B8A",
    font=("Poppins ExtraBold", 14 * -1)
)

canvas.create_text(
    320.0,
    133.0,
    anchor="nw",
    text="username",
    fill="#787B8A",
    font=("Poppins ExtraBold", 14 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pc.copy(email_area.get()),
    relief="flat"
)
button_2.place(
    x=500.0,
    y=90.0,
    width=39.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pc.copy(password_area.get()),
    relief="flat"
)
button_3.place(
    x=500.0,
    y=230.0,
    width=39.0,
    height=23.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pc.copy(username_area.get()),
    relief="flat"
)
button_4.place(
    x=500.0,
    y=161.0,
    width=39.0,
    height=23.0
)

canvas.create_text(
    70.0,
    78.0,
    anchor="nw",
    text="ValoGen",
    fill="#787B8A",
    font=("Poppins ExtraBold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
