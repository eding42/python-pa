list = []

file = open('20k.txt', 'r')

result = file.readline()

yeet = result.split(" ")

for line in yeet:
    line = line.lower()
    list.append(line)

#print(list)

#file = open("exit.py", "r")

#list = file.read()

for item in file:
    output = open("data-20k.txt", "a+")
    output.write(item)
   # output.write("\n")
    print("Finished writing {}" .format(item))
