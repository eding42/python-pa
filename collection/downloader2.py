#!/usr/bin/python3
# --- IMPORTANT NOTE ---
# Previous issues appear to have been fixed. Check here for known issues. 
# Image finding errors can be remedied by retaking the screenshot, and not changing host system brightness or coloration settings until the operation is complete, lest a new screenshot be needed. 
# Users should adjust the program according to their own use. 
'''
----- v 3.0 -----

made by Edward Ding

'''
import os
import pyautogui
import time
import random

data = open('../data/data-20k.txt','r')
temp = open("../data/temp.txt","w")

def removeLine (data,line,temp):
    temp = open("../data/temp.txt","w")    
    temp.truncate()
    print("\nRemoving used words: {}\n".format(line))
    lines = data.readlines()
    for current in lines:
        if current!= line:
            temp.write(current)
        else:
            print(current.strip('\n')+" has already been used, and will not be rewritten.")
    os.replace('../data/temp.txt','../data/data-20k.txt')

    return

#Searches for the initial text entry box
print("Searching for text entry box...\n")
first = pyautogui.locateOnScreen('text-box.png',grayscale=True)
#formats the location of the first text box
print("The boundaries of the text box are {}\n" .format(first))
textbox_center = pyautogui.center(first)
print("The center of the text box are {}\n" .format(textbox_center))

#searches for the name text entry box
print("Searching for name entry box...\n")
second = pyautogui.locateOnScreen("name-box.png",grayscale=True)
#formats the the location of the audio file name box
print("The boundaries of the title bar are {}\n" .format(second))
namebox_center = pyautogui.center(second)
print("The center of the title bar is {}\n" .format(namebox_center))
t = 0

for line in data:
    data = open('../data/data-20k.txt','r')
    #if t != 0:
    #    print("This is the first time through the loop!")
    #    for yeet1 in data:
    #        new1.append(yeet1[:-1])
    #print(new1)
    duplicate = os.path.exists('../bin/{}.wav'.format(line.strip("\n")))
    print("Checking if {} has already been processed...".format(line))
    if duplicate == False:
        print("{} has not been processed yet...".format(line))
        print('Currently working with {}\n'.format(line))
        #os.system("xdotool windowminimize $(xdotool getactivewindow)")
        print("Clicked on text entry box.")
        pyautogui.click(textbox_center.x,textbox_center.y, clicks=2,        interval=0.1, button='left')
        print("Typing in string in text entry.")
        pyautogui.typewrite(line, interval=0.2)
        pyautogui.PAUSE = 0.3
        pyautogui.click(namebox_center.x,namebox_center.y, clicks=
2, interval=0.1, button="left")
        pyautogui.typewrite(line, interval=0.2)
        pyautogui.hotkey("enter")
        print("Waiting for file to process...")
        time.sleep(1)
        x = 2
        while True:
            time.sleep(1)
            print("Waiting for {} seconds...".format(x))
            x = x + 1
            if x == 17:
                break
        #searches for the wav download link
        print("Searching for wav link...\n")
        link = pyautogui.locateOnScreen("wav.png",grayscale=True)
        #formats the the location of the wav download link
        print("The boundaries of the wav link are {}\n" .format(link))
        wavlink_center = pyautogui.center(link)
        print("The center of the wav link is {}\n" .format(wavlink_center))
        pyautogui.click(wavlink_center.x,wavlink_center.y, clicks=
1, button="left")
        print("Waiting for the download packet to be loaded")
        pyautogui.PAUSE = 10

        #searches for the save file
        #print("Searching for save file...\n")
        #save = pyautogui.locateOnScreen("savefile.png",grayscale=False)
        #formats the the location of the save file
        #print("The boundaries of the save file are {}\n" .format(save))
        #savefile_center = pyautogui.center(save)
        #print("The center of the save file is {}\n" .format(savefile_center))
        #pyautogui.click(savefile_center.x,savefile_center.y, clicks= 1, button="left")
        #pyautogui.PAUSE = 5

        pyautogui.click(734,78)
        print("Clicked on save file window")
        pyautogui.PAUSE = 1
        pyautogui.hotkey("enter")  
        #pyautogui.PAUSE = 1
        #pyautogui.hotkey("enter")  
        pyautogui.click(920,943)
        pyautogui.hotkey("enter")

        print("END of Download")

        #searches for home
        print("Searching for home...\n")
        home = pyautogui.locateOnScreen("home.png",grayscale=True)
        #formats the the location of home
        print("The boundaries of home are {}\n" .format(home))
        home_center = pyautogui.center(home)
        print("The center of home is {}\n" .format(home_center))
        pyautogui.click(home_center.x,home_center.y, clicks= 1, button="left")
        print("Traveling to home page\n")
        time.sleep(1)
        x = 2
        while True:
            time.sleep(1)
            print("Waiting for {} seconds...".format(x))
            x = x + 1
            if x == 8:
                break
        removeLine(data,line,temp)
        t = t+1
    elif duplicate == True:
        print("{}.wav already exists. Skipping...".format(line))
        removeLine(data,line,temp)
        t = t+1

data.close()
