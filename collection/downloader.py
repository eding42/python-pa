#!/usr/bin/python3
# --- IMPORTANT NOTE ---
# Only works on my XPS 13 9360, running Ubuntu 18.04 LTS at full brightness with the provided screenshots. Users should adjust the program accordingly. 

import os
import pyautogui

data = open('../data/data.txt','r')

#Searches for the initial text entry box
print("Searching for text entry box...\n")
first = pyautogui.locateOnScreen('text-box.png')
#formats the location of the first text box
print("The boundaries of the text box are {}\n" .format(first))
textbox_center = pyautogui.center(first)
print("The center of the text box are {}\n" .format(textbox_center))

#searches for the name text entry box
print("Searching for name entry box...\n")
second = pyautogui.locateOnScreen("name-box.png")
#formats the the location of the audio file name box
print("The boundaries of the title bar are {}\n" .format(second))
namebox_center = pyautogui.center(second)
print("The center of the title bar is {}\n" .format(namebox_center))

for line in data:
    print('Currently working with "{}"\n'.format(line))
    #os.system("xdotool windowminimize $(xdotool getactivewindow)")
    pyautogui.click(textbox_center.x,textbox_center.y, clicks=1, interval=0,   button='left')
    pyautogui.typewrite(line, interval=0.2)
    pyautogui.PAUSE = 0.5
    pyautogui.click(namebox_center.x,namebox_center.y, clicks=
2, interval=0.01, button="left")
    pyautogui.typewrite(line, interval=0.2)
    print("Waiting for file to process..")
    pyautogui.PAUSE = 60
