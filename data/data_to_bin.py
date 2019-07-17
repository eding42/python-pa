list = []

file = open('data.txt', 'r')

for line in file:
    line = line.lower()
    line = line[:-2]
    list.append(line)
    print("Finished writing " + line)

output = open("bin.py", "a+")
output.write(str(list))



