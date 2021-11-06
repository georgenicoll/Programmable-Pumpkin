#!/usr/bin/python

from pumpkinpi import PumpkinPi
from time import sleep

eyes = { 0, 1 }

def turn_on_or_off(leds, on_off_func):
	for index, led in enumerate(leds):
		on_off = on_off_func(index)
		if on_off:
			led.on()
		else:
			led.off()

def pump_pulse(pumpkin):
	leds = pumpkin.leds
	for x in range(10):
		turn_on_or_off(leds, lambda index: index in eyes)
		sleep(0.25)
		turn_on_or_off(leds, lambda index: not index in eyes)
		sleep(0.25)
	pumpkin.off()

def main():
	pumpkin = PumpkinPi()
	try:
		while True:
			pump_pulse(pumpkin)
			sleep(0.5)
	except KeyboardInterrupt:
		pumpkin.off()
		pumpkin.close()

if __name__ == "__main__":
	main()
