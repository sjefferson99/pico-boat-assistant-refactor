from lights.driver import Lights_Driver
from time import sleep

lights_driver = Lights_Driver()

d = 0

for light in lights_driver.lights:
    lights_driver.set_brightness(light, d)
    d += 0.06

sleep(1)

lights_driver.light_off(3)

sleep(1)

lights_driver.light_on(3)