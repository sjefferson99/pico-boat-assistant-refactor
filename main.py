from lights.driver import Lights_Driver
from time import sleep

from machine import Pin, PWM

lights_driver = Lights_Driver()

d = 0

for light in lights_driver.pwm_lights:
    lights_driver.set_brightness(light, d)
    d += 0.06