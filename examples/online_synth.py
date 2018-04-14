#!/usr/bin/env python3

import pyaudio
import wave
import time
import math
import sys
bitrate = 44100
frequency = 400
# instantiate PyAudio (1)
p = pyaudio.PyAudio()
# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = ""
    count = 0
    for x in range(frame_count):
        data += chr(count)
        count += 1
        count %= 256
    return (data, pyaudio.paContinue)
# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=bitrate,
                output=True,
                stream_callback=callback)
# start the stream (4)
stream.start_stream()
# wait for stream to finish (5)
while stream.is_active():
    time.sleep(0.1)
# stop stream (6)
stream.stop_stream()
stream.close()
wf.close()
# close PyAudio (7)
p.terminate()
