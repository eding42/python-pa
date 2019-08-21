#!/usr/bin/env python3

#from pydub import AudioSegment
#from pydub.playback import play

#song = AudioSegment.from_wav("never_gonna_give_you_up.wav")

#sound = AudioSegment.from_file("mysound.wav", format="wav")
#play(sound)



import sox

from playsound import playsound

# create combiner
cbn = sox.Combiner()

# create the output file
cbn.build(
    ['./bin/aachen.wav', './bin/aaberg.wav'], 'output.wav', 'concatenate'
)

playsound('output.wav')
