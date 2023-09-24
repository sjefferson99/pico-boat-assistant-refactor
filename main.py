from lights.driver import Lights_Driver
from time import sleep

lights_driver = Lights_Driver()

while(True):
    lights_driver.light_on()
    sleep(0.5)
    lights_driver.light_off()
    sleep(0.5)