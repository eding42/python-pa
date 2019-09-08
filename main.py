#!/usr/bin/env python3

import sox

from playsound import playsound

print("\n-------------- Welcome to python-pa v0.0.1 --------------\n")

answer = input("Please enter a string to be process.\n")

answer = answer.lower()

answer = answer.split()

print(answer)

# create combiner
cbn = sox.Combiner()

# create the output file
cbn.build(
    ['./bin/'+answer[0]+'.wav', './bin/'+answer[1]+'.wav'], 'output.wav', 'concatenate'
)

playsound('output.wav')
