## Valorant Account Creator GUI
This is a Pytho GUI application useful to create new valorant accounts in a matter of seconds with random credentials.

### About
- GUI application: easy to use and good looking
- it uses the selenium module
- the accounts' credentials are stored in a generated file called "Accounts.json"
- tested and created for Firefox, feel free to modify it for Chromium based browsers

### How to use
1) Dowload this repo
    - using **git**: `git clone https://github.com/Bbalduzz/Valorant-Account-Creator.git`
    - using the **zip**: download the zip and extract it
2) Open `ValoGen.py` and change:
    - `options.binary_location` variable (not obligatry)
        - this is the binary location of firefox, the position can change in different machines
    - `DRIVER_PATH` variable (necessary)
        - this is were `gekodriver` is downloaded, in this case it is in the folder with the script, just adjust the path
3) install the needed modules
4) Run `ValoGen.py`
5) Complete the hCaptcha test
6) Enjoy the new account

## Pictures
[ValoGen](https://i.imgur.com/SwztIJR.png)
[Show](https://i.imgur.com/LqWCGXE.mp4)

### Todo
- Add ability to autocomplete the hCaptcha test
