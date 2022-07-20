## Valorant Account Creator GUI
This is a Python GUI application useful to create new valorant accounts in a matter of seconds with random credentials.

### About
- GUI application and exeguible: easy to use and good looking
- it uses the selenium module
- the accounts' credentials are stored in a generated file called "Credentials.txt"
- tested and created for Firefox, feel free to modify it for Chromium based browsers

### How to use
#### Source code
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

#### Exeguible (.exe)
- download the **zip** file
- extract it
- enter the ValoGen folder
- run **ValoGen.exe**


## Pictures
<a href="https://imgur.com/SwztIJR"><img src="https://i.imgur.com/SwztIJR.png" title="ValoGen" /></a>
![ValoGen](https://drive.google.com/file/d/1LIbrJw4TnFJnEj1pOpdh0GUJCFNiMrVz/view?usp=sharing)

### Todo
- Add ability to autocomplete the hCaptcha test
