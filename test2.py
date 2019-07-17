import random

yeet = open("test.py" , "r")

result = eval(yeet.readline())

for line in result:
    line = random.choice(result)
    print(line)
    result.remove(line)
    print(result)
