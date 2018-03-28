#!/usr/bin/env python3
import math
import pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio

# See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 24000     #number of frames per second/frameset.      

FREQUENCY = 400     #Hz, waves per second, 261.63=C4-note.
LENGTH = 1     #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

# Generating wawes
for x in range(NUMBEROFFRAMES):
    sample = math.sin(x/((BITRATE/FREQUENCY)/math.pi))
    WAVEDATA += chr(int(sample*127+128))

for x in range(RESTFRAMES): 
    WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
