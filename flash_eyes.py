#!/usr/bin/python

#LED11 (GREEN) - 31 - 6
#LED12 (GREEN) - 32 - 12

from pumpkinpi import PumpkinPi
from time import sleep

def pump_pulse(pumpkin):
    for x in range(3):
        leds = pumpkin.leds
        leds[0].on()
        leds[1].on()
        sleep(0.25)
        leds[0].off()
        leds[1].off()
        sleep(0.25)

def main():
    pumpkin = PumpkinPi()
    try:
        while True:
            pump_pulse(pumpkin)
            sleep(0.5)
    except:
        pumpkin.off()
        pumpkin.close()

if __name__ == "__main__":
    main()
