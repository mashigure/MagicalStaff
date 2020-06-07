"""
    microbit_neopixel_test.py

    Turns on an LED in order of connected.
    This example requires a circle of 93 Neopixels (WS2812) connected to pin0.

"""
from microbit import *
import neopixel
import radio

pin1.set_pull(pin1.PULL_UP)
pin2.set_pull(pin2.PULL_UP)

# Setup the Neopixel
np = neopixel.NeoPixel(pin0, 93)

turn_off = (  0,   0,   0)
red      = (128,   0,   0)
green    = (  0, 128,   0)
blue     = (  0,   0, 128)
purple   = ( 16,   0, 128)
yellow   = (128, 128,   0)
cyan     = (  0, 128, 128)
orange   = (128,  32,   0)

sun  = (32, 35, 38, 41, 44, 47, 50, 53, 56, 58, 60, 62, 64, 66, 68, 70, 84, 85, 86, 87, 88, 89, 90, 91, 92)
star = (32, 35, 38, 41, 44, 47, 50, 53, 56, 58, 60, 62, 64, 66, 68, 70, 73, 74, 76, 77, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92)
moon = (32, 33, 34, 35, 36, 37, 38, 39, 40, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 70, 71, 72, 73, 74)

mark  = (sun, star, moon)
color = (red, yellow, purple, cyan, orange, blue, green)

words = ('Red', 'Yellow', 'Purple', 'Cyan', 'Orange', 'Blue', 'Green')

sw1 = 0
sw2 = 0
step = 0

radio.config(group=0x03)
radio.on()

while True:

    if step == 0:
        for i in range(0, len(np)): np[i] = turn_off
        np[92] = color[sw1]
    elif step == 1:
        for i in range(8): np[i+84] = color[sw1]
        sleep(64)
    elif step == 2:
        for i in range(12): np[i+72] = color[sw1]
        sleep(48)
    elif step == 3:
        for i in range(16): np[i+56] = color[sw1]
        sleep(32)
    elif step == 4:
        for i in range(24): np[i+32] = color[sw1]
        sleep(24)
    elif step == 5:
        for i in range(32): np[i] = color[sw1]
        sleep(16)
    elif step == 6:
        np[92] = turn_off
    elif step == 7:
        for i in range(8): np[i+84] = turn_off
        sleep(64)
    elif step == 8:
        for i in range(12): np[i+72] = turn_off
        sleep(48)
    elif step == 9:
        for i in range(16): np[i+56] = turn_off
        sleep(32)
    elif step == 10:
        for i in range(24): np[i+32] = turn_off
        sleep(24)
    elif step == 11:
        for i in range(32): np[i] = turn_off
        sleep(16)
    elif step == 12:
        for i in mark[sw2]: np[i] = color[sw1]
        sleep(500)

    # Display the current pixel data on the Neopixel strip
    np.show()
    sleep(10)

    radio.send(words[sw1])

    if step < 11:
        step = step + 1
    else:
        #スイッチ入力待ち
        while True:
            if pin1.read_digital() == 0:
                sw1 = (sw1+1)%7
                step = 0
                break

            if pin2.read_digital() == 0:
                radio.send('Reset')
                sw2 = (sw2+1)%3
                step = 0
                sleep(50)
                break
            
            if step == 11:
                step = 12
                break

            sleep(10)

