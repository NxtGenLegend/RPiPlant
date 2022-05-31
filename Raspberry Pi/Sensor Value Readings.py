# Temperature = Kh / Humidity
# Light  
# 
#
#

import sys
import time
import numpy as np
import Adafruit_DHT

HumPort = 1
TemPort = 2
flag = 0
frames = 10
khVal = []
khErrorVal = []

def humtemp():
    for j in range (1, 1000):
        for i in range(1, frames):
            kh = Adafruit_DHT.read(HumPort) * Adafruit_DHT.read(TemPort)
            khVal.append(kh)
            khError = (kh - np.mean(khVal))^2
            khErrorVal.append(khError)
            time.sleep(10)
        khAvg = np.mean(khVal)
        khErrorAvg = sum(khErrorVal) / frames
        for k in range(1, frames):
            kh2 = Adafruit_DHT.read(HumPort) * Adafruit_DHT.read(TemPort)
            if kh2 > khErrorAvg or kh2 < khErrorAvg:
                flag += 1
                if flag > 50:
                    return
                
# Either exit all functions or trigger warning, depending on the logical flow