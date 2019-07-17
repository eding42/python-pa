import random

data = open('../data/bin.py','r')

result = eval(data.readline())

#print(result)

for line in result:
    line = random.choice(result)
    print(line)
    result.remove(line)
