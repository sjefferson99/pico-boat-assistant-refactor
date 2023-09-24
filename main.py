from lights.driver import Lights_Driver
from time import sleep

lights_driver = Lights_Driver()

while(True):
    light = 0
    
    while light < 16:
        lights_driver.light_on(light)
        sleep(0.1)
        lights_driver.light_off(light)
        sleep(0.1)
        light += 1