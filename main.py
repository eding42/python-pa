from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")

sound = AudioSegment.from_file("mysound.wav", format="wav")
play(sound)
