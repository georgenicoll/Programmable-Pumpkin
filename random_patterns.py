from pumpkinpi import PumpkinPi
from time import sleep
import random
from spooky_display import pump_pulse as spooky_pump_pulse
from ants import pump_pulse as ants_pump_pulse
from flash_eyes import pump_pulse as flash_eyes_pump_pulse
from alternate_eyes import pump_pulse as alternate_eyes_pump_pulse
from all_on import pump_pulse as all_on_pump_pulse
from all_red import pump_pulse as all_red_pump_pulse
from random_on_off import pump_pulse as random_on_off_pump_pulse
from alternate_eyes_and_body import pump_pulse as alternate_eyes_and_body_pump_pulse
from blink_all import pump_pulse as blink_all_pump_pulse

methods = [
    spooky_pump_pulse,
    ants_pump_pulse,
    flash_eyes_pump_pulse,
    alternate_eyes_pump_pulse,
    all_on_pump_pulse,
    all_red_pump_pulse,
    random_on_off_pump_pulse,
    alternate_eyes_and_body_pump_pulse,
    blink_all_pump_pulse
]

def main():
    pumpkin = PumpkinPi(pwm=True)
    try:
        while True:
            index = random.randrange(0, len(methods))
            method = methods[index]
            method(pumpkin)
            pumpkin.off()
            sleep(0.5)
    except KeyboardInterrupt:
	    pumpkin.off()
	    pumpkin.close()

if __name__ == "__main__":
    main()

