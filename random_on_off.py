#!/usr/bin/python

from time import sleep
from pumpkinpi import PumpkinPi
import random
from signal import pause

def pump_pulse(pumpkin):
	leds = pumpkin.leds
	for x in range(10):
		for led in leds:
			on_off = random.randrange(0, 2)
			if on_off == 0:
				led.off()
			else:
				led.on()
		sleep(0.25)
	pumpkin.off()

def main():
	pumpkin = PumpkinPi(pwm=True)
	try:
		while True:
			pump_pulse(pumpkin)
			sleep(0.3)
	except KeyboardInterrupt:
		pumpkin.off()
		pumpkin.close()

if __name__ == "__main__":
	main()