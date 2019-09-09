import os
import pyautogui
import time
import random

# Testing area for module to remove already downloaded terms. 

data = open('../data/data-20k.txt','r')

def removeLine (data,line):
    print("\nRemoving used words.\n")
    lines = data.readlines()
    with open("test1.txt", "w") as f:
        for current in lines:
            if current != line:
                f.write(current)
    return

for line in data:
    duplicate = os.path.exists('..bin/{}.wav'.format(line))
    print("Checking if {} has already been processed...".format(line))
    if duplicate == False:
        removeLine(data,line)
    else:
        print("{}.wav already exists. Skipping...".format(x))
        removeLine(data,line)
