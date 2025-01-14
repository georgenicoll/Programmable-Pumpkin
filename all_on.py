#!/usr/bin/python

#LED1 - 18 - 24
#LED2 - 16 - 23
#LED3 - 15 - 22
#LED4 - 40 - 21
#LED5 - 38 - 20
#LED6 - 35 - 19
#LED7 - 12 - 18
#LED8 - 11 - 17
#LED9 - 36 - 16
#LED10 - 33 - 13
#LED11 (GREEN) - 31 - 6
#LED12 (GREEN) - 32 - 12

from pumpkinpi import PumpkinPi
from time import sleep

def pump_pulse(pumpkin):
    pumpkin.on()
    sleep(1)
    pumpkin.off()

def main():
    pumpkin = PumpkinPi()
    try:
        while True:
	        pump_pulse(pumpkin)
    except:
        pumpkin.off()
        pumpkin.close()

if __name__ == "__main__":
    main()
