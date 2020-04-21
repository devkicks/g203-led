#!env/bin/python

import os
import numpy as np
import cv2
import random
from g203_led import set_led_solid
import datetime

current_time = '{date:%Y-%m-%d_%H:%M:%S}'.format(date=datetime.datetime.now())

S = 255
V = 75


def colorToHex(r, g, b):
    return '%0.2X%0.2X%0.2X' % (r, g, b)


def generateColor(S, V):
    H = random.randint(0, 180)
    im = np.array([[[H, S, V]]], dtype=np.uint8)
    im = cv2.cvtColor(im, cv2.COLOR_HSV2RGB)
    return colorToHex(im[0, 0, 0], im[0, 0, 1], im[0, 0, 2])


if __name__ == '__main__':
    colorHex = generateColor(S, V)
    print('Setting logitech mouse color to: [%s]' % colorHex)

    try:
        set_led_solid(colorHex)
    except:
        print('Error setting color')
    
    record_file = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'history.txt')

    with open(record_file, 'a') as fp:
        fp.write(current_time + ': %s \n' % colorHex)
