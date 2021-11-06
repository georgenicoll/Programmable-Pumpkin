from pumpkinpi import PumpkinPi
from time import sleep

def pump_pulse(pumpkin):
	pumpkin.blink(.05, .05, 0, 0, 50)
	sleep(5)
	pumpkin.off()

def main():
	pumpkin = PumpkinPi(pwm=True)

	while True:
		pump_pulse(pumpkin)
		sleep(0.5)
	else:
		pumpkin.close()

if __name__ == "__main__":
	main()
