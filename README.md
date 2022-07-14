## Valorant Account Creator
This is a simple python script useful to create new valorant accounts in a matter of seconds with random credentials.

### About
- it uses the selenium module
- the accounts' credentials are stored in a generated file called "Credentials.txt"
- tested and created for Firefox, feel free to modify it for Chromium based browsers

### How to use
1) Dowload this repo
    - using **git**: `git clone https://github.com/Bbalduzz/Valorant-Account-Creator.git`
    - using the **zip**: download the zip and extract it
2) Open `main.py` and change:
    - `options.binary_location` variable
        - this is the binary location of firefox, the position can change in different machines
    - `DRIVER_PATH` variable
        - this is were `gekodriver` is downloaded, in this case it is in the folder with the script, just adjust the path
3) Run `main.py`
4) Complete the hCaptcha test
5) Enjoy the new account

### Todo
- Add ability to autocomplete the hCaptcha test
