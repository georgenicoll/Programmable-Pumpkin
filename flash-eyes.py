from pumpkinpi import PumpkinPi
from time import sleep

# Define a function to control our Pumpkin which takes a PumpkinPi as an argument.
# This script contains flashing LEDs, please take care if you are sensitive to flashing lights.
def pump_pulse(pumpkin):
    pumpkin.eyes.blink(.1, .1, 0, 0, 12) # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.
    sleep(3)
    pumpkin.off()

def main():
    pumpkin = PumpkinPi(pwm=True)
    while True:
        pump_pulse(pumpkin)
    else:
        pumpkin.close()

if __name__ == "__main__":
    main()
