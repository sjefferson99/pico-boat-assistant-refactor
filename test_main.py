from lights.driver import Lights_Driver
from time import sleep
from lights.i2c_driver import Lights_I2C_Driver

lights_driver = Lights_Driver()
lights_i2c_driver = Lights_I2C_Driver()

test_lights_driver = False
test_lights_i2c_driver = True

if test_lights_driver == True:
    d = 0

    for light in lights_driver.lights:
        lights_driver.set_brightness(light, d)
        d += 0.06

    sleep(1)

    lights_driver.light_off(3)

    sleep(1)

    lights_driver.light_on(3)

    lights_driver.light_set_brightness(0, 0.9)
    lights_driver.light_set_brightness(13, 0.1)
    
    sleep(1)

if test_lights_i2c_driver == True:
    for light in lights_driver.lights:
        lights_driver.set_brightness(light, 0)
    
    sleep(1)
    lights_i2c_driver.process_I2C(0x00) # 0x00 = light 0 on
    sleep(1)
    lights_i2c_driver.process_I2C(0x01) # 0x00 = light 1 on
    sleep(1)
    lights_i2c_driver.process_I2C(0x03) # 0x00 = light 3 on
    sleep(1)
    lights_i2c_driver.process_I2C(0x10) # 0x00 = light 0 off
    sleep(1)
    lights_i2c_driver.process_I2C(0x11) # 0x00 = light 1 off
    sleep(1)
    lights_i2c_driver.process_I2C(0x13) # 0x00 = light 3 off

    sleep(1)