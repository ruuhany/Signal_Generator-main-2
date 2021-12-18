# y = A * sin(2*pi*f*t)
#radian * 180/pi = degree

from math import exp, pi, sin
from sys import stdin
from modules import *


config = list()
eleman=['frequency', 'time', 'amplitude']
for line in stdin:
   l=line.strip()
   if l!='':
     config.append(l)

"""
======= VERIFICATION CONFIG FILE, ASSIGNING VARIABLES =======
"""
try:
    res = verification(config, eleman)
    FREQUENCY,TIME,AMPLITUDE = res 
    print(FREQUENCY,TIME,AMPLITUDE)
except ValueError:
    print('There are some errors in config File. Not enough values to unpack (expected {}, got {})'.format(len(eleman),len(res)))

# not enough values to unpack (expected 3, got 0)