#
#
#

import sys
import time
import numpy as np

DOPort = 3
flag = 0
frames = 10
kdVal = []
kdErrorVal  = []
kdconst = []

def DO():
    for j in range (1, 100)
        for i in range (1, frames):
            kdVal.append(kd)
            kdError = (kd - np.mean(kdVal))^2
            kdErrorVal.append(kdError)
            if kdErrorVal > kdconst:
                print ("too high")
            elif kdErrorVal < kdconst:
                print("too low")
            else flag += 1