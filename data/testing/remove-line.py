import os

to_remove = "3rd"

data = open("data-20.txt","r")
temp = open("temp-data-20.txt","w")


def removeLine(data, temp, to_remove):
    lines = data.readlines()    
    for current in lines:
        if current.strip('\n') != to_remove:
            temp.write(current)
        else:
            print(current.strip('\n')+" does not pass, and must be rewritten.")

removeLine(data,temp, to_remove)
