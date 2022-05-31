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
khVal = []
flag = 0

def humtemp():
    for j in range (1, 1000):
        for i in range(1, 10):
            kh = Adafruit_DHT.read(HumPort) * Adafruit_DHT.read(TemPort)
            khVal.append(kh)
            time.sleep(10)
        khAvg = np.mean(khVal)
        for k in range(1, 10):
            kh2 = Adafruit_DHT.read(HumPort) * Adafruit_DHT.read(TemPort)
            if kh2 > kh or kh2 < kh:
                flag += 1
                if flag > 50:
                    return
                
# Either exit all functions or trigger warning, depending on the logical flow